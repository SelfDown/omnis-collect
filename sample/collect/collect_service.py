# -*- coding: utf-8 -*-
"""
@Time: 2020/12/7 15:17
@Author: zzhang zzhang@cenboomh.com
@File: service.py
@desc:
"""
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# with open(sql_factory_config, 'r') as f:
#     sql_config = yaml.load(f)

from collect.utils.collect_utils import get_safe_data, is_empty, get_key, DateEncoder, getDateTime, \
    CollectServiceUtils


class CollectService:
    # 配置文件，关键字字
    const = {
        "type_name": "type",
        "key_name": "key",  #
        "module_name": "module",  # 模块名称
        "sql_file_name": "sql_file",  # sql 路径
        "sql_file_content_name": "sql_file_content",  # sql 内容
        "count_sql_name": "count_sql",
        "count_sql_param_name": "count_sql_param",
        "count_sql_file_content_name": "count_sql_file_content",  # sql 内容
        "service_dir": "service_dir",
        "data_source_name": "data_source",
        "tmp_data_source": "json",
        "json_result_name": "json_result",
        "params_name": "params",
        "params_result_name": "params_result",
        "result_extra_field": "result_extra_field",
        "data_value_name": "data_value",
        "collect_str_2_second": "collect_str_2_second",
        "collect_second_to_str": "collect_second_to_str",
        "result_parse": "result_parse",
        "data_type": "data_type",
        "excel": "excel",
        "excel_result": "excel_result",
        "sql_param_data": "sql_param_data",
        "sql_param": "sql_param",
        "sql_content": "sql_content",
        "log": "log",
        "async": "async",
        "rules": "rules",
        "key_word_rules": "key_word_rules",
        "count_params_name": "count_params",
        "count_params_result_name": "count_params_result",
        "default_name": "default",
        "exp_name": "exp",
        "format_name": "format",
        "count_name": "count",
        "template_name": "template",
        "request_rules_name": "request_rules",
        "session_user_id_name": "session_user_id",
        "params_all_name": "params_all",
        "model_file_name": "model_file",
        "django_model_name": "django_model",
        "model_name": "model",
        "exclude_save_field_name": "exclude_save_field",
        "path_name": "path",
        "class_name": "class_name",
        "check_name": "check",
        "rule_name": "rule",
        "err_msg_name": "err_msg",
        "filter_name": "filter",
        "service_name": "service",
        "service_result_name": "service_result",
        "join_name": "join",
        "result_handler_name": "result_handler",
        "method_name": "method",
        "field_name": "field",
        "remove_name": "remove",
        "reverse_name": "reverse",
        "handler_params_name": "handler_params",
        "from_field_name": "from_field",
        "to_field_name": "to_field",
        "save_field_name": "save_field",
        "foreach_name": "foreach",
        "model_field_name": "model_field",
        "must_login_name": "must_login",
        "request_handler_name": "request_handler",
        "tree_name": "tree",
        "tree_id_name": "tree_id",
        "tree_parent_name": "tree_parent",
        "value_name": "value",
        "module_handler_name": "module_handler",
        "filter_handler_name": "filter_handler",
        "name_name": "name",
        "switch_name": "switch",
        "case_name": "case",
        "switch_default_name": "switch_default",
        "enable_name": "enable",
        "before_plugin_name": "before_plugin",
        "after_plugin_name": "after_plugin",
        "exclude_name": "exclude",
        "third_application_name": "third_application",
        "from_service_name": "from_service",
        "request_register_name": "request_register",
        "session_name": "session",
        "request_name": "request",
        "header_name": "header",
        "template_log_event_id_name": "template_log_event_id",
        "template_event_log_name": "template_event_log",
        "always_name": "always",
        "data_json_name":"data_json",

    }
    router = {
        "mysql": {
            "path": "collect.service_imp.mysql.mysql_service",
            "class_name": "MysqlService"
        },

        "mysql_update": {
            "path": "collect.service_imp.mysql.mysql_update",
            "class_name": "MysqlUpdateService"
        },
        "model_save": {
            "path": "collect.service_imp.model.model_save",
            "class_name": "ModelSaveService"
        },
        "model_delete": {
            "path": "collect.service_imp.model.model_delete",
            "class_name": "ModelDeleteService"
        },
        "bulk_create": {
            "path": "collect.service_imp.model.bulk_create",
            "class_name": "BulkCreateService"
        }
    }


    def get_data_json_name(self):
        return self.const["data_json_name"]

    def get_data_json_config_path(self):
        data_json = get_safe_data(self.get_data_json_name(), self.template)

        config_dir = self.get_config_dir()
        config_file = config_dir + "/" + data_json
        return config_file

    def get_data_json(self, params):
        """
        必须实现set_json_content+get_json_content
        """
        config_file_path = self.get_data_json_config_path()
        json_content = self.get_json_content(config_file_path)
        if json_content:
            return self.success(json_content)
        data_json = get_safe_data(self.get_data_json_name(), self.template)
        data_json_result = self.get_config_file(data_json, params)
        if self.is_success(data_json_result):
            data_json_content = self.get_data(data_json_result)
            self.set_json_content(config_file_path, data_json_content)
        return data_json_result


    def setIsHttp(self, is_http):
        self.template["is_http"] = is_http

    def get_session_name(self):
        return self.const["session_name"]

    def get_always_name(self):
        return self.const["always_name"]

    def get_header_name(self):
        return self.const["header_name"]

    def get_request_name(self):
        return self.const["request_name"]

    def get_request_register_name(self):
        return self.const["request_register_name"]

    def get_from_service_name(self):
        return self.const["from_service_name"]

    def get_template_event_log_name(self):
        return self.const["template_event_log_name"]

    def get_render_tool(self):
        from collect.service_imp.common.filters.template_tool import TemplateTool
        tool = TemplateTool(op_user=self.op_user)
        return tool

    def get_config_file(self, config_file_name, params):
        config_dir = self.get_config_dir()
        config_file = config_dir + "/" + config_file_name
        import os
        if not os.path.exists(config_file):
            self.log(config_file + "不存在", "error", self.template)
            return self.fail(config_file + "文件不存在")
        with open(config_file, 'r') as f:
            config_file_content = f.read()
        key_word_rules = self.get_key_word_rules()
        for key_word in key_word_rules:
            config_rule = key_word_rules[key_word]
            path = config_rule["path"]
            class_name = config_rule["class_name"]
            import importlib
            key_rule_class = importlib.import_module(path)
            key_rule_class = getattr(key_rule_class, class_name)()
            rule_result = key_rule_class.handler(self.template, config_file_content, params, config_rule, config_dir)
            if not self.is_success(rule_result):
                return rule_result
            config_file_content = self.get_data(rule_result)
        return self.success(config_file_content)

    def get_exclude_name(self):
        return self.const["exclude_name"]

    def get_module_handler_name(self):
        return self.const["module_handler_name"]

    def is_enable(self, params, node):
        from collect.service_imp.common.filters.template_tool import TemplateTool
        template_tool = TemplateTool(op_user=self.op_user)
        enable = get_safe_data(self.get_enable_name(), node)
        if enable:
            enable_value = template_tool.render(enable, params)
            if enable_value == self.get_false_value():
                return False
        return True

    def get_before_plugin_name(self):
        return self.const["before_plugin_name"]

    def get_after_plugin_name(self):
        return self.const["after_plugin_name"]

    def get_third_application_name(self):
        return self.const["third_application_name"]

    def set_config_params(self, config_params, template=None):
        template = self.get_template_data(template)
        template[self.get_params_name()] = config_params

    def get_switch_name(self):
        return self.const["switch_name"]

    def get_case_name(self):
        return self.const["case_name"]

    def get_name_name(self):
        return self.const["name_name"]

    def get_true_value(self):
        return "True"

    def get_false_value(self):
        return "False"

    def get_tree_id_name(self):
        return self.const["tree_id_name"]

    def get_tree_parent_name(self):
        return self.const["tree_parent_name"]

    def get_tree_name(self):
        return self.const["tree_name"]

    def get_request_handler_name(self):
        return self.const["request_handler_name"]

    def get_enable_name(self):
        return self.const["enable_name"]

    def get_must_login_name(self):
        return self.const["must_login_name"]

    def get_filter_handler_name(self):
        return self.const["filter_handler_name"]

    def get_switch_default_name(self):
        return self.const["switch_default_name"]

    def get_render_data(self, templ, params, tool, nullToTemplateField=True):
        """
        nullToTemplateField 如果值为空则设置模板的变量，一般用于检查字段是否设置值
        """
        # if templ in params:
        #     return params[templ]
        # else:
        #     return tool.render(str(templ), params)
        # 如果配置的值存在，参数中，就取参数
        # 匹配第一级
        field_arr = templ.split(".")
        if templ in params:
            value = params[templ]
        # 匹配第二级
        elif len(field_arr) == 2 and field_arr[0] in params and field_arr[1] in params[field_arr[0]]:
            value = params[field_arr[0]][field_arr[1]]
        elif self.is_template_text(templ):
            value = tool.render(templ, params)
        else:
            # 如果里面 . 在里面
            # if len(field_arr) >0:
            #     value = ""
            # else:
            # 允许没有找到值，则设置模板字段
            if nullToTemplateField:
                value = templ
            else:
                value = ""
        return value

    def get_update_fields(self, model_obj,
                          param_result=None,
                          update_fields=None,
                          exclude_save_field=None,
                          ):
        if not param_result:
            param_result = self.get_params_result()
        fields_list = []

        def can_save_field(field):
            has_attr = hasattr(model_obj, field)
            return has_attr

        has = False
        for key in param_result:
            if not can_save_field(key):
                continue

            if exclude_save_field and key in exclude_save_field:
                continue
            if update_fields and key not in update_fields:
                continue
            has = True
            fields_list.append(key)
        if self.can_log() and not has:
            self.log("没有找到任何更新属性请检查配置")
        return fields_list

    def update_field(self, model_obj, params=None):
        if not params:
            param_result = self.get_params_result()
        else:
            param_result = params

        update_fields = self.get_update_fields(model_obj, param_result)
        if len(update_fields) == 0:
            return self.fail(self.get_template_service_name() + " 没有找到任何更新属性")
        for key in update_fields:
            value = param_result[key]
            setattr(model_obj, key, value)
        return self.success(model_obj)

    def get_node_service(self, node, params=None, template=None, append_param=True, nullToTemplateField=True):
        service = get_safe_data(self.get_service_name(), node)
        if not params:
            params = self.get_params_result()

        if not service:
            import json
            return self.fail(json.dumps(node, cls=DateEncoder) + "节点没有找到" + self.get_service_name())
        # 处理service 的参数
        from collect.service_imp.common.filters.template_tool import TemplateTool
        template_tool = TemplateTool(op_user=self.op_user)
        for key in service:
            if key == self.get_service_name():
                continue
            value_template = service[key]
            value = self.get_render_data(value_template, params, template_tool, nullToTemplateField)
            service[key] = value
        # 拼接其他参数

        if append_param:
            exclude = ["SFTPClient", "SSHClient"]
            for key in params:
                if key not in service:
                    t = type(params[key]).__name__
                    if t in exclude:
                        continue
                    service[key] = params[key]
        return self.success(service)

    def get_get_template_method_name(self):
        return "get_template_method"

    def get_set_template_method_name(self):
        return "set_template_method"

    def handler_self_register_data(self, service_obj, template=None):
        """
        将数据从上级往下级传递，优先模板
        """
        request_register = self.get_request_register()
        for register in request_register:
            path = register[self.get_path_name()]
            class_name = register[self.get_class_name()]
            try:
                get_data_method = getattr(self, register[self.get_get_template_method_name()])
                register_data = get_data_method(template)
                set_data_method = getattr(service_obj, register[self.get_set_template_method_name()])
                set_data_method(register_data)
            except Exception as e:
                return self.fail(class_name + "找不到，请检查配置" + str(e))

    def get_service_result(self, service, template=None):
        """
            调用模板服务
        """
        import time
        start = time.time()

        from collect.service.template_service import TemplateService
        template_service = TemplateService(op_user=self.op_user)
        template_service.set_session(self.get_session())
        self.handler_self_register_data(template_service, template)

        # request_register = self.get_request_register()
        # for register in request_register:
        #     path = register[self.get_path_name()]
        #     class_name = register[self.get_class_name()]
        #     try:
        #         get_data_method = getattr(self, register["get_template_method"])
        #         register_data = get_data_method(template)
        #         set_data_method = getattr(template_service, register["set_template_method"])
        #         set_data_method(register_data)
        #     except Exception as e:
        #         return self.fail(class_name + "找不到，请检查配置" + str(e))

        template_result = template_service.result(service)

        end = time.time()
        if template and self.can_log(template):
            service_name = get_safe_data(self.get_service_name(), service)
            msg = "请求 {service} 服务 耗时 {spend} 秒".format(service=service_name, spend=str(end - start))
            self.log(msg, template=template)
        return template_result

    def get_from_field_name(self):
        return self.const["from_field_name"]

    def get_save_field_name(self):
        return self.const["save_field_name"]

    def get_foreach_name(self):
        return self.const["foreach_name"]

    def get_to_field_name(self):
        return self.const["to_field_name"]

    def get_model_field_name(self):
        return self.const["model_field_name"]

    def get_reverse_name(self):
        return self.const["reverse_name"]

    def get_field_name(self):
        return self.const["field_name"]

    def get_remove_name(self):
        return self.const["remove_name"]

    def get_rule_name(self):
        return self.const["rule_name"]

    def get_err_msg_name(self):
        return self.const["err_msg_name"]

    def get_service_result_name(self):
        return self.const["service_result_name"]

    def get_path_name(self):
        return self.const["path_name"]

    def get_join_name(self):
        return self.const["join_name"]

    def get_class_name(self):
        return self.const["class_name"]

    def get_count_name(self):
        return self.const["count_name"]

    def get_session_user_id_name(self):
        return self.const["session_user_id_name"]

    def get_params_all_name(self):
        return self.const["params_all_name"]

    def get_filter_name(self):
        return self.const["filter_name"]

    def get_method_name(self):
        return self.const["method_name"]

    def get_result_handler_name(self):
        return self.const["result_handler_name"]

    def get_handler_params_name(self):
        return self.const["handler_params_name"]

    def get_service_name(self):
        return self.const["service_name"]

    def get_key_name(self):
        return self.const["key_name"]

    def get_template_service_name(self, template=None):
        template_data = self.get_template_data(template)
        if template_data:
            return get_safe_data(self.get_key_name(), template_data)
        return ""

    def get_params_name(self):
        return self.const["params_name"]

    def get_params_result_name(self):
        return self.const["params_result_name"]

    def get_params_result(self, template=None):
        if not template:
            template = self.template
        return get_safe_data(self.get_params_result_name(), template, {})

    def set_params_result(self, params, template=None):
        if not template:
            template = self.template
        template[self.get_params_result_name()] = params

    def get_count_params_name(self):
        return self.const["count_params_name"]

    def get_count_params_result_name(self):
        return self.const["count_params_result_name"]

    def get_count_params_result(self):
        return get_safe_data(self.get_count_params_result_name(), self.template)

    def set_count_params_result(self, params, template=None):
        if not template:
            template = self.template
        template[self.get_count_params_result_name()] = params

    def get_excel_result_name(self):
        return self.const["excel_result"]

    def get_log_name(self):
        return self.const["log"]

    def get_async_name(self):
        return self.const["async"]

    def get_service_dir_name(self):
        return self.const["service_dir"]

    def get_rules_name(self):
        return self.const["rules"]

    def get_key_word_rules_name(self):
        return self.const["key_word_rules"]

    def get_django_model_name(self):
        return self.const["django_model_name"]

    def get_request_rules_name(self):
        return self.const["request_rules_name"]

    def get_exp_name(self):
        return self.const["exp_name"]

    def get_format_name(self):
        return self.const["format_name"]

    def get_check_name(self):
        return self.const["check_name"]

    def get_template_name(self):
        return self.const["template_name"]

    def get_value_name(self):
        return self.const["value_name"]

    def is_async(self):
        return True == get_safe_data(self.get_async_name(), self.template)

    def can_log(self, template=None):
        if not template:
            template = self.template
        return True == get_safe_data(self.get_log_name(), template)

    def get_template_result(self, template_str, params, config_params=None, template=None):
        import copy
        params = copy.copy(params)
        from collect.service_imp.common.filters.template_tool import TemplateTool
        template_tool = TemplateTool(op_user=self.op_user)
        params_result = self.get_params_result(template)
        if params_result and self.get_params_result_name() not in params:
            params[self.get_params_result_name()] = params_result
        # value = template_tool.render(template_str, params, config_params, template)
        value = self.get_render_data(template_str, params, template_tool)
        return self.success(value)

    def get_node_template_result(self, node, params, field="template", config_params=None, template=None):
        if not template:
            template = self.template
        import json

        name = get_safe_data(self.get_name_name(), node)
        switch = get_safe_data(self.get_switch_name(), node)
        switch_default = get_safe_data(self.get_switch_default_name(), node)
        if self.can_log(template):
            self.log(node, template=template)
        if switch and isinstance(switch, list):
            if self.can_log(template):
                self.log("获取switch 判断", template=template)
            for item in switch:
                case = get_safe_data(self.get_case_name(), item)
                templ = get_safe_data(field, item)
                if not case:
                    return self.fail(name + ":" + self.get_case_name() + "字段不存在")
                if not templ:
                    return self.fail(name + ":" + self.get_template_name() + "字段不存在")
                case_result = self.get_template_result(case, params, config_params=config_params, template=template)
                if self.can_log(template):
                    self.log(case, template=template)
                    self.log(templ, template=template)
                    self.log(case_result, template=template)
                    self.log(case_result, template=template)

                if not self.is_success(case_result):
                    return case_result
                case_data = self.get_data(case_result)
                if case_data == self.get_true_value():
                    return self.get_template_result(templ, params, config_params=config_params, template=template)

            if switch_default:
                return self.get_template_result(switch_default, params, config_params=config_params, template=template)

        if field not in node:
            return self.fail(name + ":" + field + "字段不存在")
        template_str = node[field]
        return self.get_template_result(template_str, params, config_params=config_params, template=template)

    def get_sql_param_data_name(self):
        """
        sql 参数数据字段
        :return:
        """
        return self.const["sql_param_data"]

    def get_sql_param_name(self):
        """
        sql 参数 key 字段
        :return:
        """
        return self.const["sql_param"]

    def get_count_sql_param_name(self):
        """
        sql 参数 key 字段
        :return:
        """
        return self.const["count_sql_param_name"]

    def get_sql_content_name(self):
        """
        sql 内容
        :return:
        """
        return self.const["sql_content"]

    def get_data_value_rule(self):
        return get_safe_data(self.get_data_value_name(), self.template)

    def filter_result_value(self, result):
        """

        :param result:
        :return:
        """

    def get_data_value_name(self):
        return self.const["data_value_name"]

    def get_data_type_name(self):
        return self.const["data_type"]

    def get_type_name(self):
        return self.const["type_name"]

    def get_result_extra_field(self):
        return get_safe_data(self.get_result_extra_field_name(), self.template, {})

    def get_result_extra_field_name(self):
        return self.const["result_extra_field"]

    def get_excel_config_name(self):
        return self.const["excel"]

    def xml_to_plain_text(self, xml):
        import html2text
        xml = html2text.html2text(xml)
        return xml

    def get_template_params(self):
        return get_safe_data(self.get_params_name(), self.template)

    def get_sql_content(self):
        from collect.service_imp.config_data.config_cache_data import ConfigCacheData
        return ConfigCacheData.get_sql(self.get_sql_key())
        # return get_safe_data(self.get_sql_file_content_name(), self.template)

    def get_count_sql_content(self):
        return get_safe_data(self.get_count_sql_file_content_name(), self.template)

    def get_config_dir(self):
        config_dir = get_safe_data(self.get_service_dir_name(), self.template)
        return config_dir

    def get_sql_key(self):
        """
        文件路径作为key
        :return:
        """
        return str(get_safe_data(self.get_service_dir_name(), self.template)) + "#" + str(
            get_safe_data(self.get_sql_file_name(), self.template))

    def get_count_sql_key(self):
        """
        文件路径作为key
        :return:
        """
        return str(get_safe_data(self.get_service_dir_name(), self.template)) + "#" + str(
            get_safe_data(self.get_count_sql_file(), self.template))

    def set_sql_content(self, sql_content):
        # sql_file_content_name = self.get_sql_file_content_name()
        # self.template[sql_file_content_name] = sql_content
        from collect.service_imp.config_data.config_cache_data import ConfigCacheData
        ConfigCacheData.set_sql(self.get_sql_key(), sql_content)

    def get_request_register(self):
        from collect.service_imp.config_data.config_cache_data import ConfigCacheData
        return ConfigCacheData.get_request_register()

    def get_always_request_register(self):
        registers = self.get_request_register()
        for item in registers:
            if get_safe_data(self.get_always_name(), item):
                return item
        return

    def get_before_plugin(self):
        from collect.service_imp.config_data.config_cache_data import ConfigCacheData
        return ConfigCacheData.get_before_plugin()

    def get_after_plugin(self):
        from collect.service_imp.config_data.config_cache_data import ConfigCacheData
        return ConfigCacheData.get_after_plugin()

    def get_request_handler(self):
        from collect.service_imp.config_data.config_cache_data import ConfigCacheData
        return ConfigCacheData.get_request_handler()

    def set_count_sql_content(self, sql_content):
        # count_sql_file_content_name = self.get_count_sql_file_content_name()
        # self.template[count_sql_file_content_name] = sql_content
        from collect.service_imp.config_data.config_cache_data import ConfigCacheData
        ConfigCacheData.set_sql(self.get_count_sql_key(), sql_content)

    @staticmethod
    def is_template_text(text):
        if "{{" in text or "{%" in text:
            return True
        return False

    def is_template_node(self, node):
        switch = get_safe_data(self.get_switch_name(), node, False)
        template = get_safe_data(self.get_template_name(), node, False)
        return switch or template

    def get_tmp_result(self):
        if self.is_tmp_data_source():
            """
            支持显示临时数据，配置字符串以json 格式返回
            """

            data = get_safe_data(self.get_json_result_name(), self.template)
            try:
                import json
                return json.loads(data)
            except Exception as e:
                return data
        else:
            return

    def get_json_result_name(self):
        return self.const["json_result_name"]

    def is_tmp_data_source(self):
        """
        如果是临时数据，显示配置数据
        :return:
        """

        data_source = self.get_data_source()
        return data_source == self.const["tmp_data_source"]

    def get_data_source(self):
        data_source_name = self.get_data_source_name()
        data_source = get_safe_data(data_source_name, self.template)
        return data_source

    def get_data_source_name(self):
        return self.const["data_source_name"]

    def get_module_name(self):
        return self.const["module_name"]

    def get_sql_file_name(self):
        return self.const["sql_file_name"]

    def get_sql_file_content_name(self):
        return self.const["sql_file_content_name"]

    def get_count_sql_file_content_name(self):
        return self.const["count_sql_file_content_name"]

    def get_count_sql_name(self):
        return self.const["count_sql_name"]

    def get_count_sql_file(self):
        return get_safe_data(self.get_count_sql_name(), self.template)

    def is_empty_count_sql(self):
        return is_empty(self.get_count_sql_name(), self.template)

    def get_result_parse_name(self):
        return self.const["result_parse"]

    def get_excel_config(self):
        return get_safe_data(self.get_excel_config_name(), self.template, {})

    def get_result_parse(self):

        rule_name = get_safe_data(self.get_result_parse_name(), self.template, {})
        return get_safe_data(rule_name, self.get_rules())

    def __init__(self, op_user=None):

        from collect.utils.log import get_collect_log
        self.logger = get_collect_log()
        self.op_user = op_user
        self.template_log_event_id = None
        self.template = {}
        self.request = None
        self.load_router()

        self.finish = True

        self.session = None
        self.header = None
        # 初始化模板事件

        pass

    # def add_template_event_log(self, log_type, data):
    #     self.template_event_log.add_template_event(log_type, data)
    #     pass

    def setIsHttp(self, is_http):
        self.template["is_http"] = is_http

    def set_header(self, header):
        self.header = header
        self.template[self.get_header_name()] = header

    def get_template_log_event_id_name(self):
        return self.const["template_log_event_id_name"]

    def set_template_log_event_id(self, template_log_event_id):
        self.template_log_event_id = template_log_event_id
        self.template[self.get_template_log_event_id_name()] = template_log_event_id

    def set_session(self, session):
        self.template[self.get_session_name()] = session
        self.session = session

    def get_session(self, template=None):
        if template:
            return template[self.get_session_name()]
        return self.session

    def get_request(self, template=None):
        if template:
            return template[self.get_request_name()]
        return self.request

    def set_request(self, request):
        self.request = request
        self.template[self.get_request_name()] = request

    def get_header(self, template=None):
        if template:
            return template[self.get_header_name()]
        return self.header

    def get_template_log_event_id(self, template=None):
        if template:
            return template[self.get_template_log_event_id_name()]
        return self.template_log_event_id

    def log(self, msg, level=None, template=None):

        event_id = self.get_template_log_event_id(template)
        if event_id:
            from collect.service_imp.template_event_log.template_event_log import template_log
            template_log.add_template_event(self.get_template_event_log_name(), {
                "user_id": self.op_user,
                "event_id": event_id,
                "msg": msg,
                "datetime": getDateTime("%Y-%m-%d %H:%M:%S.%f"),
                "from_service": self.get_template_service_name(template)
            })
            write_file_log = get_key("write_file_log", "true")
            if write_file_log != "true":
                return

        if isinstance(msg, dict):
            import json
            try:
                msg = json.dumps(msg, cls=DateEncoder, ensure_ascii=False)
            except Exception as e:
                msg = json.dumps(msg, cls=DateEncoder, encoding="ISO-8859-1", ensure_ascii=False)

        if not level:
            self.logger.info(msg)
        elif level == "error":
            self.logger.error(msg)
        elif level == "warn":
            self.logger.warn(msg)

    def get_items_router(self):
        from collect.service_imp.config_data.config_cache_data import ConfigCacheData
        return ConfigCacheData.get_router_config()

    def get_rules(self):
        # global rules
        # return rules
        from collect.service_imp.config_data.config_cache_data import ConfigCacheData
        return ConfigCacheData.get_rules()

    def get_third_application(self, name):
        """
        获取第三方应用
        :param name:
        :return:
        """
        from collect.service_imp.config_data.config_cache_data import ConfigCacheData
        third_application = ConfigCacheData.get_third_application()
        if third_application:
            config = get_safe_data(name, third_application)
            if config:
                app_config = {}
                for item in config:
                    app_config[get_safe_data(self.get_key_name(), item)] = item
                return app_config

    def set_template(self, template):
        # 复制模板
        """
        这个千万不要乱改，已经验证过，将copy 去掉必报错，因为模板被改了
        """
        import copy
        self.template = copy.deepcopy(template)

    def get_django_model_config(self):
        from collect.service_imp.config_data.config_cache_data import ConfigCacheData
        return ConfigCacheData.get_django_model_config()

    def get_result_handler(self):
        from collect.service_imp.config_data.config_cache_data import ConfigCacheData
        return ConfigCacheData.get_result_handler()

    def get_module_handler(self):
        from collect.service_imp.config_data.config_cache_data import ConfigCacheData
        return ConfigCacheData.get_module_handler()

    def get_filter_handler(self):
        from collect.service_imp.config_data.config_cache_data import ConfigCacheData
        return ConfigCacheData.get_filter_handler()

    def get_template(self):
        return self.template

    def get_key_word_rules(self):
        from collect.service_imp.config_data.config_cache_data import ConfigCacheData
        return ConfigCacheData.get_key_word_rules()

    def get_request_rules(self):
        from collect.service_imp.config_data.config_cache_data import ConfigCacheData
        return ConfigCacheData.get_request_rules()

    def handler_rules(self, router_all):

        if is_empty(self.get_rules_name(), router_all):
            rules = {}
            return
        rules = get_safe_data(self.get_rules_name(), router_all)
        return rules

    def handler_key_word_rules(self, router_all):

        if is_empty(self.get_key_word_rules_name(), router_all):
            key_word_rules = {}
            return
        key_word_rules = get_safe_data(self.get_key_word_rules_name(), router_all)
        return key_word_rules

    def handler_request_handler(self, router_all):
        """
         加载请求处理器规则
        :param router_all:
        :return:
        """
        handler_name = self.get_request_handler_name()
        if is_empty(handler_name, router_all):
            return
        request_handlers = get_safe_data(handler_name, router_all)
        request_handler_dict = {}
        for handler in request_handlers:
            key = get_safe_data(self.get_key_name(), handler)
            request_handler_dict[key] = handler
        return request_handler_dict

    def handler_result_handler(self, router_all):
        """
         加载请求处理器规则
        :param router_all:
        :return:
        """
        handler_name = self.get_result_handler_name()
        if is_empty(handler_name, router_all):
            return
        request_handlers = get_safe_data(handler_name, router_all)
        result_handler_dict = {}
        for handler in request_handlers:
            key = get_safe_data(self.get_key_name(), handler)

            result_handler_dict[key] = handler
        return result_handler_dict

    def handler_module_handler(self, router_all):
        """
         加载模块处理器规则
        :param router_all:
        :return:
        """
        handler_name = self.get_module_handler_name()
        if is_empty(handler_name, router_all):
            return
        module_handlers = get_safe_data(handler_name, router_all)
        module_handler_dict = {}
        for handler in module_handlers:
            key = get_safe_data(self.get_key_name(), handler)
            module_handler_dict[key] = handler
        return module_handler_dict

    def handler_filter_handler(self, router_all):
        """
         加载模块自定义处理器规则
        :param router_all:
        :return:
        """
        handler_name = self.get_filter_handler_name()
        if is_empty(handler_name, router_all):
            return
        filter_handlers = get_safe_data(handler_name, router_all)
        filter_handler_dict = {}
        for handler in filter_handlers:
            key = get_safe_data(self.get_key_name(), handler)
            filter_handler_dict[key] = handler
        return filter_handler_dict

    def handler_before_plugin_handler(self, router_all):
        """
         加载请求插件
        :param router_all:
        :return:
        """
        handler_name = self.get_before_plugin_name()
        if is_empty(handler_name, router_all):
            return
        filter_handlers = get_safe_data(handler_name, router_all)
        return filter_handlers

    def handler_after_plugin_handler(self, router_all):
        """
         加载请求插件
        :param router_all:
        :return:
        """
        handler_name = self.get_after_plugin_name()
        if is_empty(handler_name, router_all):
            return
        filter_handlers = get_safe_data(handler_name, router_all)
        return filter_handlers

    def handler_request_register(self, router_all):
        """
         处理 请求的request 对象
        """
        handler_name = self.get_request_register_name()
        if is_empty(handler_name, router_all):
            return
        filter_handlers = get_safe_data(handler_name, router_all)
        return filter_handlers

    def handler_third_application_handler(self, router_all):
        """
         加载第三方应用
        :param router_all:
        :return:
        """
        handler_name = self.get_third_application_name()
        if is_empty(handler_name, router_all):
            return
        filter_handlers = get_safe_data(handler_name, router_all)
        return filter_handlers

    def handler_django_model(self, router_all):
        """
         加载配置的模型地址
        :param router_all:
        :return:
        """

        if is_empty(self.get_django_model_name(), router_all):
            django_model = ""
            return
        django_model = get_safe_data(self.get_django_model_name(), router_all)
        return django_model

    def get_model_file_name(self):
        return self.const["model_file_name"]

    def get_model_file(self):
        return get_safe_data(self.get_model_file_name(), self.get_django_model_config())

    def get_model_name(self):
        return self.const["model_name"]

    def get_model(self):
        return get_safe_data(self.get_model_name(), self.template)

    def get_model_class(self):
        path = self.get_model_file()
        class_name = self.get_model()
        if not class_name:
            self.log("没有找到" + self.get_model_name() + "配置")
            return
        import importlib
        model_factory = importlib.import_module(path)
        model_class = getattr(model_factory, class_name)
        return model_class

    def get_model_obj(self):
        model_class = self.get_model_class()
        model_obj = model_class()
        if not model_obj:
            class_name = self.get_model()
            return self.fail(class_name + "对象没有找到")
        return self.success(model_obj)

    def handler_request_rules(self, router_all):
        if is_empty(self.get_key_word_rules_name(), router_all):
            request_rules = {}
            return
        request_rules = get_safe_data(self.get_request_rules_name(), router_all)
        return request_rules

    def handler_services(self, router_all, excel_data_path):
        """
        处理服务
        :return:
        """
        if is_empty("services", router_all):
            self.log(excel_data_path + "配置文件没有找到 services 节点")
        services = router_all["services"]
        import os
        collect_data_dir = os.path.dirname(excel_data_path)
        router_dict = {}
        # 拼接文件
        for project_service in services:
            project_key = project_service["key"]
            path = project_service["path"]
            project_path = collect_data_dir + "/" + path
            project_router = {}
            if not os.path.exists(project_path):
                self.log(project_path + "不存在")
                continue
            with open(project_path, 'r') as f:
                import yaml
                project_router = yaml.load(f)
            if is_empty("service", project_router):
                self.log(project_path + "配置文件没有找到 service 节点", "error")
                continue

            service = project_router["service"]
            for index, item in enumerate(service):
                if project_key not in router_dict:
                    router_dict[project_key] = []
                if is_empty("path", item):
                    self.log(project_path + "配置文件 第 " + str((index + 1)) + " 节点 没有找到 path 节点")
                    continue
                # 配置对应的目录
                config_dir = os.path.dirname(project_path)
                path = config_dir + "/" + item["path"]
                router_dict[project_key].append(path)

        router_result_dict = {}
        for key in router_dict:
            files = router_dict[key]
            if key not in router_result_dict:
                router_result_dict[key] = {}
            current_project_dict = router_result_dict[key]
            for config in files:
                config_keys = {}
                if not os.path.exists(config):
                    self.log(config + "不存在", "error")
                    continue
                with open(config, 'r') as f:
                    import yaml
                    config_keys = yaml.load(f)
                if is_empty("service", config_keys):
                    self.log(config + "配置文件没有找到 service 节点")
                    continue

                service = config_keys["service"]
                service_dir = os.path.dirname(config)
                for index, item in enumerate(service):
                    item_key = item["key"]
                    item[self.get_service_dir_name()] = service_dir
                    if item_key in router_result_dict[key]:
                        self.log(key + "." + item_key + "服务已经存在")
                        continue
                    if is_empty("module", item):
                        self.log(config + "配置文件 第" + str(index) + "节点 没有找到 module 节点")
                        continue

                    current_project_dict[item_key] = item
        return router_result_dict

    def get_config_data(self):
        from collect.service_imp.config_data.config_cache_data import ConfigCacheData
        router_config = ConfigCacheData.get_router_config()
        return router_config

    def load_router(self):
        """
          1.加载路由，设置些全局规则，比如路由规则、请求字段规则、数据转换规则、django 模型规则。
          2.子类通过调用get具体的规则方法，或者配置，来获取配置的值。比如get_django_model,是django 模型的配置
          3.所有规则都缓存在 ConfigCacheData ，实际是全局变量，将来可以可以改成redis 缓存、获取其他缓存，
          4.目前ConfigCacheData只存了写简单json 对象，切记不要缓存，python 对象，避免将来不能迁移到其他缓存架构
        :return:
        """
        from collect.service_imp.config_data.config_cache_data import ConfigCacheData
        router_config = ConfigCacheData.get_router_config()
        if router_config:
            return

        collect_file_path = get_key("collect_file_path")
        self.log("加载配置文件：" + collect_file_path)
        with open(collect_file_path, 'r') as f:
            import yaml
            router_all = yaml.load(f)
        # 设置路由转换规则
        router_config = self.handler_services(router_all, collect_file_path)
        ConfigCacheData.set_router_config(router_config)
        # 设置数据结果转换规则
        rules = self.handler_rules(router_all)
        ConfigCacheData.set_rules(rules)
        # 设置关键字规则
        key_word_rules = self.handler_key_word_rules(router_all)
        ConfigCacheData.set_key_word_rules(key_word_rules)
        # 设置请求规则
        request_rules = self.handler_request_rules(router_all)
        ConfigCacheData.set_request_rules(request_rules)
        # 设置django 模型规则
        django_model = self.handler_django_model(router_all)
        ConfigCacheData.set_django_model_config(django_model)
        # 处理请求处理器
        self.log("加载请求处理")
        request_handler = self.handler_request_handler(router_all)
        ConfigCacheData.set_request_handler(request_handler)
        self.log("加载结果处理器")
        result_handler = self.handler_result_handler(router_all)
        ConfigCacheData.set_result_handler(result_handler)
        self.log("加载模块处理器")
        module_handler = self.handler_module_handler(router_all)
        ConfigCacheData.set_module_handler(module_handler)
        self.log("加载jinja2模板自定义函数")
        filter_handler = self.handler_filter_handler(router_all)
        ConfigCacheData.set_filter_handler(filter_handler)
        self.log("加载请求插件")
        before_plugin = self.handler_before_plugin_handler(router_all)
        ConfigCacheData.set_before_plugin(before_plugin)

        self.log("加载结果插件")
        after_plugin = self.handler_after_plugin_handler(router_all)
        ConfigCacheData.set_after_plugin(after_plugin)

        self.log("加载第三方应用")
        third_application = self.handler_third_application_handler(router_all)
        ConfigCacheData.set_third_application(third_application)
        self.log("加载请求注册器")
        request_register = self.handler_request_register(router_all)
        ConfigCacheData.set_request_register(request_register)

    def fail(self, msg):
        return CollectServiceUtils.fail(msg=msg)

    def combine_other(self, other, result):
        now = CollectServiceUtils.get_other(result)
        if not now and not other:
            return None

        if not other:
            other = {}
        for key in now:
            if key not in other:
                other[key] = now[key]
        return other

    def success(self, data, count=-1, msg="", finish=False, other=None):
        return CollectServiceUtils.success(data=data, msg=msg, count=count, finish=finish, other=other)

    def get_other(self, result):
        return CollectServiceUtils.get_other(result)

    def is_success(self, data):
        return CollectServiceUtils.is_success(data)

    def is_finish(self, data):
        return CollectServiceUtils.is_finish(data)

    def get_msg(self, data):
        return CollectServiceUtils.get_msg(data)

    def get_data(self, data):
        return CollectServiceUtils.get_data(data)

    def get_count(self, data):
        return CollectServiceUtils.get_count(data)

    def make_service(self, service):
        result = self.get_module(service)
        if not self.is_success(result):
            return result
        data = self.get_data(result)
        module_name = get_safe_data(self.get_module_name(), data)
        module_handler = self.get_module_handler()
        if module_name not in module_handler:
            return self.fail("没有实现 " + module_name)
        module = module_handler[module_name]
        path = module[self.get_path_name()]
        class_name = module[self.get_class_name()]
        import importlib
        collect_factory = importlib.import_module(path)
        collect_obj = getattr(collect_factory, class_name)(op_user=self.op_user)
        collect_obj.set_template(data)
        # collect_obj.set_session(self.get_session())
        return self.success(data=collect_obj)

    def get_default_name(self):
        return self.const["default_name"]

    def handler_type_values(self, params, config_params):
        # import json
        # params = json.loads(json.dumps(params))
        import copy
        params = copy.deepcopy(params)
        # # 替换请求参数
        for key in params:
            config_param = get_safe_data(key, config_params)
            if not config_param:
                continue
            value = params[key]
            data_type = get_safe_data(self.get_type_name(), config_param)
            if data_type:
                if data_type == "bool":
                    try:
                        if value == 'false':
                            value = False
                        elif value == 'true':
                            value = True
                        params[key] = value
                    except Exception as e:
                        self.logger.error("字段{key} 值{value}。转bool 类型错误" + str(e))
                        pass

                if data_type == 'int':
                    try:
                        value = int(value)
                        params[key] = value
                    except Exception as e:
                        self.logger.error("字段{key} 值{value}。转int 类型错误" + str(e))
                        pass
            if self.get_default_name() in config_param and str(value) == "":
                params[key] = config_param[self.get_default_name()]
        params[self.get_session_user_id_name()] = self.op_user
        # 编写默认值
        for key in config_params:
            config_param = get_safe_data(key, config_params)
            if not config_param:
                continue

            if self.get_default_name() in config_param and key not in params:
                params[key] = config_param[self.get_default_name()]
        # import copy
        # params[self.get_params_all_name()] = copy.deepcopy(params)
        return self.success(params)

    # def handler_check_values(self,params,config_params):

    def handler_rules_values(self, params, config_params, template=None):
        """
        处理数据转换规则
        :param params:
        :param config_params:
        :return:
        """
        # rules = self.get_request_rules()
        template = self.get_template_data(template)
        rules = self.get_request_rules()
        for rule in rules:
            import importlib
            path = rule[self.get_path_name()]
            class_name = rule[self.get_class_name()]
            collect_factory = importlib.import_module(path)
            rule_obj = getattr(collect_factory, class_name)(op_user=self.op_user)
            result = rule_obj.handler(params, config_params, template=template)
            if not self.is_success(result):
                return result

        return self.success(params)

    def handler_params(self, params, config_params, template=None):
        """

        :param params: 请求参数
        :param config_params:  配置参数
        :return:
        """
        # 处理请求参数
        result = self.handler_type_values(params, config_params)
        if not self.is_success(result):
            return result
        params = self.get_data(result)
        # 处理数据转换规则
        result = self.handler_rules_values(params, config_params, template)
        if not self.is_success(result):
            return result
        params = self.get_data(result)

        return self.success(params)

    def get_template_data(self, template):
        if template:
            return template
        else:
            return self.template

    def get_config_params(self, template=None):
        template = self.get_template_data(template)
        config_params = get_safe_data(self.get_params_name(), template, {})
        return config_params

    def handler_req_count_params(self, params, req_params, template=None):
        import copy
        params = copy.copy(params)
        template = self.get_template_data(template)
        count_config_params = get_safe_data(self.get_count_params_name(), template)
        if not count_config_params:
            return self.success({})
        # 删除配置请求
        for key in req_params:
            if key in count_config_params:
                del params[key]
        count_params = self.handler_params(params, count_config_params, template)
        count_params = self.get_data(count_params)
        # 复制请求参数不存在的配置
        for key in req_params:
            if key not in count_params:
                count_params[key] = req_params[key]
        return self.success(count_params)

    def handler_req_params(self, params, template=None):
        template = self.get_template_data(template)
        config_params = get_safe_data(self.get_params_name(), template, {})
        return self.handler_params(params, config_params, template)

    def handler_result(self):
        """
        处理结果
        :return:
        """

    def login_check(self):
        must_login = True
        if self.get_must_login_name() in self.template:
            must_login = self.template[self.get_must_login_name()]
        if must_login and self.op_user == '-1':
            self.log(self.get_template_service_name())
            return self.fail(msg="请重新登录")
        else:
            return self.success(data=[])

    def before_result(self, params):
        """
        执行前
        :return:
        """
        if self.can_log():
            self.log(self.op_user + "访问" + self.get_template_service_name())
            import json
            try:
                # tmp = json.dumps(params, cls=DateEncoder)
                self.log(params)
            except Exception as e:
                pass

        if self.get_before_plugin():
            from collect.service_imp.before_plugin.before_plugin import BeforePlugin
            before_plugin = BeforePlugin(op_user=self.op_user)
            plugin_result = before_plugin.handler(params, self.template)
            if not self.is_success(plugin_result) or self.is_finish(plugin_result):
                return plugin_result

        return self.success(params)

    def after_result(self, result):
        """
         处理结果
        :param result:
        :return:
        """
        msg = ""
        other = None
        if self.get_after_plugin():
            from collect.service_imp.after_plugin.after_plugin import AfterPlugin
            after_plugin = AfterPlugin(op_user=self.op_user)
            plugin_result = after_plugin.handler(result, self.template)
            if not self.is_success(plugin_result) or self.is_finish(plugin_result):
                return plugin_result
            # 设置消息
            plugin_msg = self.get_msg(plugin_result)
            if plugin_msg:
                msg = plugin_msg
            # 设置其他域
            plugin_other = self.get_other(plugin_result)
            if plugin_other:
                other = plugin_other
            # 设置数据
            result = self.get_data(plugin_result)
        return self.success(result, msg=msg, other=other)

    def result(self, params):

        # 获取临时数据配置
        tmp_result = self.get_tmp_result()
        # 如果有数据返回则是临时数据
        if tmp_result:
            self.finish = True
            return self.success(tmp_result)
        else:
            self.finish = False
            return self.success(tmp_result)

    def is_file_result(self):
        data_type = get_safe_data(self.get_data_type_name(), self.template)
        if data_type == "file":
            return True
        else:
            return False

    def filter_result_obj(self, result):
        """
        处理转换对象，添加而外字段
        :param result:
        :return:
        """

        rule = self.get_result_parse()
        if rule:
            path = rule[self.get_path_name()]
            class_name = rule[self.get_class_name()]
            import importlib
            rule_factory = importlib.import_module(path)
            rule_obj = getattr(rule_factory, class_name)()
            return rule_obj.get_result_obj(result, self.template)
        return self.success(result)

    # def result_data(self):
    #     return []

    def get_module(self, service):
        arr = service.split(".")
        if len(arr) < 2:
            return self.fail("服务名称格式有误")
        collect_project = arr[0]
        collect_item = arr[1]
        item_router = self.get_items_router()
        if collect_project not in item_router:
            return self.fail(collect_project + "项目不存在")
        collect_project_config = item_router[collect_project]
        if collect_item not in collect_project_config:
            return self.fail(collect_item + "服务不存在")
        return self.success(collect_project_config[collect_item])
