# -*- coding: utf-8 -*-
"""
@Time: 2020/12/8 11:15
@Author: zzhang zzhang@cenboomh.com
@File: mysql_service.py
@desc:
"""
from collect.collect_service import CollectService
from collect.utils.collect_utils import is_empty, get_safe_data, sqlToData, connection_sql_to_data, \
    close_old_connections_wrapper


class SqlService(CollectService):
    def __init__(self, op_user):
        CollectService.__init__(self, op_user)

        pass

    def sql_file2sqlContent(self, sql_file, params):
        config_file_result = self.get_config_file(sql_file, params)
        if not self.is_success(config_file_result):
            self.log(self.get_msg(config_file_result), level="error")
            return
        return self.get_data(config_file_result)

    def content2Sql(self, sql_content, params, to_param_key=True, from_config=False):
        """

        :param sql_content: sql 内容
        :param params: 参数
        :param to_param_key: 保持变量
        :param from_config: 变量来着配置
        :return:
        """
        if not params:
            params = {}
        from jinja2 import Environment

        def get_template_vars(templ):
            if not templ:
                return []

            env = Environment()
            parsed_content = env.parse(templ)
            content = parsed_content.body
            result = []

            def get_node(node):
                var_name_list = []

                def get_param_obj(param_key, param_value=None, child_param_keys=None):
                    """

                    """
                    # 数组对象
                    if child_param_keys:
                        from collect.service_imp.sql.sql_param.array_obj_param import ArrayObjParam
                        return ArrayObjParam(param_key, param_value, child_param_keys)
                    # 简单数组
                    if param_key in params and isinstance(params[param_key], list):
                        from collect.service_imp.sql.sql_param.array_param import ArrayParam
                        return ArrayParam(param_key, param_value, child_param_keys)
                    # 普通值
                    else:
                        from collect.service_imp.sql.sql_param.normal_param import NormalParam
                        return NormalParam(param_key, param_value, child_param_keys)

                from jinja2.nodes import For, Name, Output, If, Getattr
                # 处理子是否包含变量
                if isinstance(node, Output):
                    for node_item in node.nodes:
                        var_name_list += get_node(node_item)

                # 处理表层变量
                elif isinstance(node, Name):
                    var_name_list.append(get_param_obj(node.name))
                # 处理if else
                elif isinstance(node, If):
                    for l in "body", "elif_", "else_":
                        var_name_list += get_nodes(node, l)
                elif isinstance(node, For):
                    arr_list = []
                    # 获取for里面的字符串
                    arr_list += [node_item.nodes for node_item in node.body if isinstance(node_item, Output)]
                    att_var_list = []
                    # 获取属性列表
                    for item in arr_list:
                        att_var_list += [node_arr for node_arr in item if isinstance(node_arr, Getattr)]
                    # 获取字段
                    fields = [item.attr for item in att_var_list]
                    # 生成数组对象
                    var_name_list.append(get_param_obj(node.iter.name, child_param_keys=fields))

                return var_name_list

            def get_nodes(parent_node, name):
                node_list = []
                if not hasattr(parent_node, name):
                    return node_list
                body = getattr(parent_node, name)
                for child in body:
                    node_list += get_node(child)
                return node_list

            for item in content:
                result += get_node(item)
            return result

        vars = get_template_vars(sql_content)

        # 变量赋值 %s
        template_params = {}
        # 渲染已经配置的模板变量
        for p in vars:
            param_key = p.get_param_key()
            # 如果变量没有值，则不进行渲染
            if is_empty(param_key, params):
                continue
            pkv = params[param_key]
            # 必须先设置值，然后进行值判断
            p.set_param_value(pkv)
            # 获取变量值
            param_key_value = p.get_param_key_value(to_param_key)
            # 设置变量值
            template_params[param_key] = param_key_value
            # # 如果是非数组对象变量，则跳过
            # if not p.is_array():
            #     continue
            # 设置数组对象的值
            key_list = p.get_param_key_list()
            # 渲染新的模板变量值
            for arr_key_param in key_list:
                # 设置变量值
                template_params[p.get_attr_name_value(arr_key_param)] = p.get_attr_value_name_value(arr_key_param)
        real_values = []
        for p in vars:
            param_key = p.get_param_key()
            # 如果变量没有值，则不进行渲染
            if is_empty(param_key, params):
                continue
            real_values += p.get_real_value()
        # 其他字段直接copy
        for key in params:
            if key not in template_params:
                template_params[key] = params[key]
        from collect.service_imp.common.filters.template_tool import TemplateTool
        tool = TemplateTool(self.op_user)
        result_content = self.get_render_data(sql_content, template_params, tool)
        return result_content, template_params, real_values

    def template2Sql(self, sql_content, params, from_config=False):

        try:
            # 转换为变量
            result_content, template_params, real_values = self.content2Sql(sql_content, params, True, from_config)
            # 转换为sql的占位符
            result_content, t1, real_values = self.content2Sql(result_content, template_params, False, from_config)
            # 去掉html
            # result_content = self.xml_to_plain_text(result_content)
            data = {
                self.get_sql_content_name(): result_content,
                self.get_sql_param_name(): real_values
            }
            return self.success(data)
        except Exception as e:
            return self.fail(str(e) + " : sql 解析错误")

    def get_sql(self, from_config=False):
        """
        这里只解析2级模板变量，意思是不支持if标签 里面在套用 if 标签
        :param params:  前台参数
        :param param_from:  生成sql 参数来着配置文件，还是请求参数
        :return:
        """
        sql_content = self.get_sql_content()
        count_sql_content = self.get_count_sql_content()

        # 如果存在sql,解析sql。如果是第一次加载，则从文件中获取。第二次缓存
        if not sql_content:
            sql_file = get_safe_data(self.get_sql_file_name(), self.template)
            sql_file_content = self.sql_file2sqlContent(sql_file, self.get_params_result())
            self.set_sql_content(sql_file_content)
            sql_content = sql_file_content

        sql_result = self.template2Sql(sql_content, self.get_params_result(), from_config)
        if not self.is_success(sql_result):
            return sql_result
        sql_result = self.get_data(sql_result)
        if not self.is_empty_count_sql() and not count_sql_content:
            count_sql_file = get_safe_data(self.get_count_sql_name(), self.template)
            sql_count_file_content = self.sql_file2sqlContent(count_sql_file, self.get_count_params_result())
            self.set_count_sql_content(sql_count_file_content)
            count_sql_content = sql_count_file_content
        # 设置统计sql
        if count_sql_content:
            count_sql_result = self.template2Sql(count_sql_content, self.get_count_params_result(), from_config)
            if not self.is_success(count_sql_result):
                return count_sql_result
            count_sql_result = self.get_data(count_sql_result)
            sql_result[self.get_count_sql_name()] = count_sql_result[self.get_sql_content_name()]
            sql_result[self.get_count_sql_param_name()] = count_sql_result[self.get_sql_param_name()]
        return self.success(sql_result)

    def result_sql(self, result):
        """
        获取sql
        :param result:
        :return:
        """
        return result[self.get_sql_content_name()]

    def result_count_sql(self, result):
        """
        获取sql
        :param result:
        :return:
        """
        return result[self.get_count_sql_name()]

    def result_param(self, result):
        """
        获取参数
        :param result:
        :return:
        """
        return result[self.get_sql_param_data_name()]

    def result_param_name_list(self, result):
        """
        获取参数key 列表
        :param result:
        :return:
        """
        return result[self.get_sql_param_name()]

    def result_count_param_name_list(self, result):
        """
        获取count参数key 列表
        :param result:
        :return:
        """
        return result[self.get_count_sql_param_name()]

    @close_old_connections_wrapper
    def result(self, params=None):
        result = CollectService.result(self, params)
        if self.finish or not self.is_success(result):
            return result

        sql_result = self.get_sql()
        if not self.is_success(sql_result):
            return sql_result
        sql_result = self.get_data(sql_result)
        sql = self.result_sql(sql_result)
        # 获取参数
        param_data = self.result_param_name_list(sql_result)
        if self.can_log():
            self.log(sql)
            self.log(param_data)
        data_source = self.get_data_source()
        try:
            result = connection_sql_to_data(sql, param_data, datasource=data_source)
        except Exception as e:
            self.log("=======================================", "error")
            self.log(str(e), "error")
            self.log("=======================================", "error")
            self.log(sql, "error")
            self.log(param_data, "error")

            return self.fail("sql 执行异常:【" + sql + "】" + str(e))
        count = 0
        if not self.is_empty_count_sql():
            count_sql = self.result_count_sql(sql_result)
            count_params = self.get_count_params_result()
            count_param_data = self.result_count_param_name_list(sql_result)

            if self.can_log():
                self.log(count_sql)
                self.log(count_param_data)
            count_data = connection_sql_to_data(count_sql, count_param_data, datasource=data_source)
            if len(count_data) > 0:
                count_data = count_data[0]
                count = get_safe_data(self.get_count_name(), count_data)

        return self.success(result, count=count)
