# -*- coding: utf-8 -*-
import json

from collect.service_imp.request_handlers.request_handler import RequestHandler
from collect.utils.collect_utils import get_safe_data


class GetModifyData(RequestHandler):
    """
     比较修改的数据
    """
    gmd_const = {
        "fields_name": "fields",
        "rule_name": "rule",
        "left_name": "left",
        "right_name": "right",
        "left_save_field_name": "left_save_field",
        "right_save_field_name": "right_save_field",
        "transfer_name": "transfer",
        "current_value_field_name": "current_value_field",
        "operation_name": "operation",
        "add_name": "add",
        "remove_name": "remove",
        "modify_name": "modify",
        "item_field_name": "item_field",
        "left_array_item_name": "left_array_item",
        "right_array_item_name": "right_array_item",

    }

    def get_left_array_item_name(self):
        return self.gmd_const["left_array_item_name"]

    def get_right_array_item_name(self):
        return self.gmd_const["right_array_item_name"]

    def get_fields_name(self):
        return self.gmd_const["fields_name"]

    def get_item_field_name(self):
        return self.gmd_const["item_field_name"]

    def get_operation_name(self):
        return self.gmd_const["operation_name"]

    def get_transfer_name(self):
        return self.gmd_const["transfer_name"]

    def get_rule_name(self):
        return self.gmd_const["rule_name"]

    def get_right_name(self):
        return self.gmd_const["right_name"]

    def get_left_name(self):
        return self.gmd_const["left_name"]

    def get_left_save_field_name(self):
        return self.gmd_const["left_save_field_name"]

    def get_right_save_field_name(self):
        return self.gmd_const["right_save_field_name"]

    def get_current_value_field_name(self):
        return self.gmd_const["current_value_field_name"]

    def get_modify_name(self):
        return self.gmd_const["modify_name"]

    data_json_dict = {}

    def get_add_operation(self):
        return self.gmd_const["add_name"]

    def get_remove_operation(self):
        return self.gmd_const["remove_name"]

    @staticmethod
    def get_json_content(path):
        return get_safe_data(path, GetModifyData.data_json_dict)

    @staticmethod
    def set_json_content(path, data_json_content):
        GetModifyData.data_json_dict[path] = data_json_content

    def handler(self, params, config, template):
        data_json_path = get_safe_data(self.get_data_json_name(), config)
        if not data_json_path:
            return self.fail(self.get_data_json_name() + "字段不存在")
        rules = self.get_data_json(params, data_json_path, template)
        if not self.is_success(rules):
            return rules
        params_result = self.get_params_result(template)

        rules = self.get_data(rules)
        rules = json.loads(rules)
        # 必须配置fields
        fields = get_safe_data(self.get_fields_name(), rules)
        if not fields:
            return self.fail(data_json_path + "配置文件中没有配置" + self.get_fields_name())
        # 必须配置left_save_field
        left_save_field = get_safe_data(self.get_left_save_field_name(), rules)
        if not left_save_field:
            return self.fail("没有找打配置" + self.get_left_save_field_name())
            # 必须配置right_save_field
        right_save_field = get_safe_data(self.get_right_save_field_name(), rules)
        if not right_save_field:
            return self.fail("没有找打配置" + self.get_right_save_field_name())
        result_list = []
        # 获取结果
        for index, rule in enumerate(fields):
            rule_name = get_safe_data(self.get_rule_name(), rule)
            if not rule_name:
                return self.fail(data_json_path + "配置文件中第" + str(index + 1) + "条规则没有配置" + self.get_rule_name())
            result = None
            name = get_safe_data(self.get_name_name(), rule)
            field = get_safe_data(self.get_field_name(), rule)
            if not field:
                msg = self.get_error_msg(field, name, index, self.get_field_name() + "字段不存在")
                return self.fail(msg)
            if not name:
                msg = self.get_error_msg(field, name, index, self.get_name_name() + "字段不存在")
                return self.fail(msg)

            left_name = get_safe_data(self.get_left_name(), rule)
            # 必须传left
            if not left_name:
                msg = self.get_error_msg(field, name, index, self.get_left_name() + "字段不存在")
                return self.fail(msg)
            # 必须传right
            right_name = get_safe_data(self.get_right_name(), rule)
            if not right_name:
                msg = self.get_error_msg(field, name, index, self.get_right_name() + "字段不存在")
                return self.fail(msg)

            if rule_name == 'compare_field_value':
                """
                 处理简单值比较
                """
                result = self.handler_compare_field_value(params_result, rule, left_save_field, right_save_field,
                                                          template)
            elif rule_name == 'compare_array_add_delete':
                """
                处理数组的新增和删除
                """
                result = self.handler_compare_array_add_delete(params_result, rule, left_save_field, right_save_field,
                                                               template)
            elif rule_name == 'compare_array_modify':
                """
                处理数组中同一个值的变化
                """
                result = self.handler_compare_array_modify(params_result, rule, left_save_field, right_save_field,
                                                           template)

            if not result:
                continue
            if not self.is_success(result):
                msg = self.get_error_msg(field, name, index, self.get_msg(result))
                return self.fail(msg)
            result_data = self.get_data(result)
            if result_data:
                result_list += result_data

        # 处理保存字段
        save_field = get_safe_data(self.get_save_field_name(), config)
        if save_field:
            params[save_field] = result_list
        return self.success(params)

    def get_error_msg(self, field, name, index, msg):
        return "第 " + str(index + 1) + "个规则 【" + self.get_field_name() + ":" + str(field) + "】(" + str(
            name) + ") :" + str(msg)

    def handler_compare_array_modify(self, params, rule, left_save_field, right_save_field, template):
        """
        处理数组的的新增和删除
        """
        key_templ = get_safe_data(self.get_key_name(), rule)
        if not key_templ:
            msg = self.get_key_name() + "字段不存在"
            return self.fail(msg)
        item_field_name = get_safe_data(self.get_item_field_name(), rule)
        if not item_field_name:
            msg = self.get_item_field_name() + "字段不存在"
            return self.fail(msg)
        left_array_item_name = get_safe_data(self.get_left_array_item_name(), rule)
        if not left_array_item_name:
            msg = self.get_left_array_item_name() + "字段不存在"
            return self.fail(msg)
        right_array_item_name = get_safe_data(self.get_right_array_item_name(), rule)
        if not right_array_item_name:
            msg = self.get_right_array_item_name() + "字段不存在"
            return self.fail(msg)
        fields = get_safe_data(self.get_fields_name(), rule)
        if not fields:
            msg = self.get_fields_name() + "字段不存在"
            return self.fail(msg)
        for index, field in enumerate(fields):
            value_templ = get_safe_data(self.get_value_name(), field)
            if not value_templ:
                msg = "第 " + str(index + 1) + "字段规则【" + self.get_value_name() + "】字段不存在"
                return self.fail(msg)

            templ = get_safe_data(self.get_template_name(), field)
            if not templ:
                msg = "第 " + str(index + 1) + "字段规则【" + self.get_template_name() + "】字段不存在"
                return self.fail(msg)
            name = get_safe_data(self.get_name_name(), field)
            if not name:
                msg = "第 " + str(index + 1) + "字段规则【" + self.get_name_name() + "】字段不存在"
                return self.fail(msg)
            field = get_safe_data(self.get_field_name(), field)
            if not field:
                msg = "第 " + str(index + 1) + "字段规则【" + self.get_field_name() + "】字段不存在"
                return self.fail(msg)

        from collect.service_imp.common.filters.template_tool import TemplateTool
        tool = TemplateTool(self.op_user)
        left = self.render_data(get_safe_data(self.get_left_name(), rule), params, tool)
        right = self.render_data(get_safe_data(self.get_right_name(), rule), params, tool)
        # 获取删除的
        left_dict = {}
        right_common_list = []
        for item in left:
            p = {item_field_name: item}
            key = self.render_data(key_templ, p)
            left_dict[key] = item
        for item in right:
            p = {item_field_name: item}
            key = self.render_data(key_templ, p)
            if key in left_dict:
                right_common_list.append(item)

        right_dict = {}
        left_common_list = []
        for item in right:
            p = {item_field_name: item}
            key = self.render_data(key_templ, p)
            right_dict[key] = item
        for item in left:
            p = {item_field_name: item}
            key = self.render_data(key_templ, p)
            if key in right_dict:
                left_common_list.append(item)

        right_common_list.sort(key=lambda item: self.render_data(key_templ, {item_field_name: item}))
        left_common_list.sort(key=lambda item: self.render_data(key_templ, {item_field_name: item}))
        result_list = []
        for left_item, right_item in zip(left_common_list, right_common_list):
            for field in fields:
                p = {
                    left_array_item_name: left_item,
                    right_array_item_name: right_item
                }
                templ = get_safe_data(self.get_template_name(), field)
                value_templ = get_safe_data(self.get_value_name(), field)
                name = get_safe_data(self.get_name_name(), field)
                field_name = get_safe_data(self.get_field_name(), field)
                result = self.render_data(templ, p)
                if result != self.get_true_value():
                    left_value = self.render_data(value_templ, left_item)
                    right_value = self.render_data(value_templ, right_item)
                    obj_result = self.get_obj(left_save_field, right_save_field, left_value, right_value, rule,
                                              template, operation=self.get_modify_name(), name=name, field=field_name)
                    if not self.is_success(obj_result):
                        return obj_result
                    result_list = [self.get_data(obj_result)]

        return self.success(result_list)

    def handler_compare_array_add_delete(self, params, rule, left_save_field, right_save_field, template):
        """
        处理数组的的新增和删除
        """
        templ = get_safe_data(self.get_key_name(), rule)
        if not templ:
            msg = self.get_key_name() + "字段不存在"
            return self.fail(msg)
        item_field_name = get_safe_data(self.get_item_field_name(), rule)
        if not item_field_name:
            msg = self.get_item_field_name() + "字段不存在"
            return self.fail(msg)
        value_templ = get_safe_data(self.get_value_name(), rule)
        if not value_templ:
            msg = self.get_value_name() + "字段不存在"
            return self.fail(msg)
        from collect.service_imp.common.filters.template_tool import TemplateTool
        tool = TemplateTool(self.op_user)
        left = self.render_data(get_safe_data(self.get_left_name(), rule), params, tool)
        right = self.render_data(get_safe_data(self.get_right_name(), rule), params, tool)
        right_dict = {}

        for item in right:
            p = {item_field_name: item}
            key = self.render_data(templ, p)
            right_dict[key] = item
        # 获取新增的
        add_list = []
        for item in left:
            p = {item_field_name: item}
            key = self.render_data(templ, p)
            if key not in right_dict:
                add_list.append(item)
        # 获取删除的
        left_dict = {}
        remove_list = []
        for item in left:
            p = {item_field_name: item}
            key = self.render_data(templ, p)
            left_dict[key] = item
        for item in right:
            p = {item_field_name: item}
            key = self.render_data(templ, p)
            if key not in left_dict:
                remove_list.append(item)

        result_list = []
        for item in add_list:
            p = {item_field_name: item}
            left = self.render_data(value_templ, p)
            obj_result = self.get_obj(left_save_field, right_save_field, left, "", rule, template,
                                      self.get_add_operation())
            if not obj_result:
                return self.fail(obj_result)
            result_list.append(self.get_data(obj_result))

        for item in remove_list:
            p = {item_field_name: item}
            right = self.render_data(value_templ, p)
            obj_result = self.get_obj(left_save_field, right_save_field, "", right, rule, template,
                                      self.get_remove_operation())
            if not obj_result:
                return self.fail(obj_result)
            result_list.append(self.get_data(obj_result))

        return self.success(result_list)

    def handler_compare_field_value(self, params, rule, left_save_field, right_save_field, template):
        """
        处理普通字段
        """

        # 必须传 template
        templ = get_safe_data(self.get_template_name(), rule)
        if not templ:
            msg = self.get_template_name() + "字段不存在"
            return self.fail(msg)
        from collect.service_imp.common.filters.template_tool import TemplateTool
        tool = TemplateTool(self.op_user)
        left = self.render_data(get_safe_data(self.get_left_name(), rule), params, tool)
        right = self.render_data(get_safe_data(self.get_right_name(), rule), params, tool)
        data_dict = {
            self.get_left_name(): left,
            self.get_right_name(): right,
        }
        # 计算结果
        result = self.get_render_data(templ, data_dict, tool)
        result_list = []
        if result != self.get_true_value():
            obj_result = self.get_obj(left_save_field, right_save_field, left, right, rule, template)
            if not self.is_success(obj_result):
                return obj_result
            result_list = [self.get_data(obj_result)]
        return self.success(result_list)

    def get_obj(self, left_save_field, right_save_field, left, right, rule, template, operation=None, name=None,
                field=None):
        # 保存处理转换

        transfer = get_safe_data(self.get_transfer_name(), rule)
        if not field:
            field = get_safe_data(self.get_field_name(), rule)
        if not operation:
            operation = get_safe_data(self.get_operation_name(), rule)
        if not operation:
            return self.fail(field + "没有获取到操作，请检查是否配置：" + self.get_operation_name())
        if transfer:
            if not get_safe_data(self.get_service_name(), transfer):
                return self.fail(self.get_transfer_name() + "没有配置" + self.get_service_name())

            # service_node = get_safe_data(self.get_service_name(), transfer)
            def transferValue(value):
                compare_field_value = get_safe_data(self.get_current_value_field_name(), transfer,
                                                    "compare_field_value")
                p = {
                    compare_field_value: value
                }
                # 构造一个服务
                import copy
                service = self.get_node_service(copy.deepcopy(transfer), p, template)
                if not self.is_success(service):
                    return service
                service = self.get_data(service)
                # 运行服务的结果
                service_result = self.get_service_result(service, template)
                if not self.is_success(service_result):
                    return service_result
                data = self.get_data(service_result)
                # 获取服务数据

                save_field = get_safe_data(self.get_save_field_name(), transfer)
                if not save_field:
                    return self.fail(
                        "【" + field + "】" + self.get_transfer_name() + "中没有配置" + self.get_save_field_name())
                # 取变量值
                value_temp = get_safe_data(self.get_value_name(), transfer)
                if not save_field:
                    return self.fail("【" + field + "】" + self.get_transfer_name() + "中没有配置" + self.get_value_name())
                p2 = {save_field: data}
                value = self.render_data(value_temp, p2)
                return self.success(value)

            left_result = transferValue(left)
            if not self.is_success(left_result):
                return left_result
            left = self.get_data(left_result)
            right_result = transferValue(right)
            if not self.is_success(right_result):
                return right_result
            right = self.get_data(right_result)
        if not name:
            name = get_safe_data(self.get_name_name(), rule)
        obj = {
            self.get_operation_name(): operation,
            left_save_field: left,
            right_save_field: right,
            self.get_field_name(): field,
            self.get_name_name(): name
        }

        # obj[self.get_transfer_name()] = transfer
        return self.success(obj)
