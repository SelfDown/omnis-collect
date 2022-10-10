# -*- coding: utf-8 -*-
import json

from collect.service_imp.request_handlers.request_handler import RequestHandler
from collect.utils.collect_utils import get_safe_data


class BaseModifyRule:

    def __init__(self, params,
                 rule,
                 left_save_field,
                 right_save_field,
                 template,
                 renderFunction,
                 tool,
                 get_node_service,
                 get_service_result,

                 ):
        self.params = params
        self.rule = rule
        self.left_save_field = left_save_field
        self.right_save_field = right_save_field
        self.template = template
        self.render_data = renderFunction
        self.tool = tool
        self.get_node_service = get_node_service
        self.get_service_result = get_service_result

    def render(self, templ, params, nullToTemplateField=False):
        "渲染变量"
        return self.render_data(templ, params, self.tool, nullToTemplateField=nullToTemplateField)

    def get_template_name(self):
        return "template"

    def get_templ(self):
        "获取渲染的模板变量"
        return get_safe_data(self.get_template_name(), self.rule)

    def get_field_name(self):
        return "field"

    def get_field(self, rule=None):
        "获取渲染的模板变量"
        if not rule:
            rule = self.rule
        return get_safe_data(self.get_field_name(), rule)

    def get_left_name(self):
        return "left"

    def get_rule_name(self):
        return "rule"

    def get_right_name(self):
        return "right"

    def get_name_name(self):
        return "name"

    def get_obj_left(self):
        "获取左边对象"
        # 如果left 没有配置，则取整个参数
        obj = None
        rule = self.rule
        templ = get_safe_data(self.get_left_name(), rule)
        # 如果没有模板变量，直接去参数
        if not templ:
            obj = self.params
        else:
            obj = self.render(templ, self.params)
        # 如果是数组变量则，取字段
        return self.handler_field_obj(rule, obj)

    def is_array_rule(self, rule):
        rule_name = get_safe_data(self.get_rule_name(), rule)
        if rule_name in ("compare_array_modify", "compare_array_add_delete"):
            return True
        else:
            return False

    def handler_field_obj(self, rule, obj):
        field = self.get_field(rule)
        if self.is_array_rule(rule) and field in obj:
            return obj[field]
        return obj

    def get_obj_right(self):
        "获取右边对象"
        rule = self.rule
        templ = get_safe_data(self.get_right_name(), rule)
        obj = self.render(templ, self.params)
        # 如果是数组变量则，取字段
        return self.handler_field_obj(rule, obj)

    def get_operation_name(self):
        return "operation"

    def get_append_original_item_name(self):
        return "append_original_item"

    def get_append_right_fields_name(self):
        return "append_right_fields"

    def get_value_name(self):
        return "value"

    def get_value_templ(self, rule=None):
        if not rule:
            rule = self.rule
        value_templ = get_safe_data(self.get_value_name(), rule)
        return value_templ

    def get_data(self, data):
        return get_safe_data("data", data)

    def is_success(self, data):
        return data["success"] == True

    def get_save_field_name(self):
        return "save_field"

    def get_enable_name(self):
        return "enable"

    def get_operation(self, rule=None):
        if rule:
            return get_safe_data(self.get_operation_name(), rule)
        return get_safe_data(self.get_operation_name(), self.rule)

    def is_enable_rule(self, rule=None):
        if not rule:
            rule = self.rule
        enable = get_safe_data(self.get_enable_name(), rule)
        if not enable:
            return True
        return self.render(enable, self.params) == self.get_true_value()

    def get_field_value(self, data=None, rule=None):
        if not data:
            data = self.get_obj_left()
        value_templ = self.get_value_templ(rule)
        if not value_templ:
            value_templ = self.get_field(rule)
        value = self.render(value_templ, data)
        if value is None:
            return ""
        else:
            return value

    def get_left_value(self):
        return get_safe_data(self.get_field(), self.get_obj_left())

    def get_right_value(self):
        return get_safe_data(self.get_field(), self.get_obj_right())

    def get_transfer_name(self):
        return "transfer"

    def get_transfer(self, rule=None):
        if not rule:
            rule = self.rule
        return get_safe_data(self.get_transfer_name(), rule)

    def get_service_name(self):
        return "service"

    def get_modify_name(self):
        return "modify"

    def get_add_operation(self):
        return "add"

    def get_remove_operation(self):
        return "remove"

    def _get_obj(self, left, right, rule, operation=None, transfer_dict=None):
        if not operation:
            operation = self.get_operation(rule)
        left_value = self.get_field_value(left, rule)
        right_value = self.get_field_value(right, rule)
        transfer = self.get_transfer(rule)
        if transfer:
            if not get_safe_data(self.get_service_name(), transfer):
                return self.get_transfer_name() + "没有配置" + self.get_service_name(), False

            # service_node = get_safe_data(self.get_service_name(), transfer)
            def transferValue(value):
                if transfer_dict is not None:
                    transfer_value = get_safe_data(value, transfer_dict, "")
                    return transfer_value, True
                compare_field_value = get_safe_data("compare_field_value", transfer,
                                                    "compare_field_value")
                p = {
                    compare_field_value: value
                }
                # 构造一个服务
                import copy
                service = self.get_node_service(copy.deepcopy(transfer), p, self.template)
                if not self.is_success(service):
                    return service
                service = self.get_data(service)
                # 运行服务的结果

                service_result = self.get_service_result(service, self.template)
                if not self.is_success(service_result):
                    return service_result
                data = self.get_data(service_result)
                # 获取服务数据

                save_field = get_safe_data(self.get_save_field_name(), transfer)
                if not save_field:
                    return "【" + self.get_field() + "】" + self.get_transfer_name() + "中没有配置" + self.get_save_field_name(), False
                # 取变量值
                value_temp = get_safe_data(self.get_value_name(), transfer)
                if not save_field:
                    return "【" + self.get_field() + "】" + self.get_transfer_name() + "中没有配置" + self.get_value_name(), False
                p2 = {save_field: data}
                value = self.render(value_temp, p2)
                return value, True

            # 处理如果是删除，则左边没有值，不必从数据库查询，直接滞空
            if operation != self.get_remove_operation():
                left_result, success = transferValue(left_value)
                if not success:
                    return left_result, success
                left_value = left_result
            else:
                left = ""
            if operation != self.get_add_operation():
                right_result, success = transferValue(right_value)
                if not success:
                    return right_result, success
                right_value = right_result
            else:
                right_value = ""
        obj = {
            self.get_operation_name(): operation,
            self.left_save_field: left_value,
            self.right_save_field: right_value,
            self.get_field_name(): self.get_field(),
            self.get_name_name(): get_safe_data(self.get_name_name(), rule)
        }
        append_original_item = get_safe_data(self.get_append_original_item_name(), rule, False)
        # 拼接原始的数据
        if append_original_item:
            if operation == self.get_remove_operation():
                obj = dict(right.items() + obj.items())
            else:
                obj = dict(left.items() + obj.items())

        # 拼接右边的数据
        append_right_fields = get_safe_data(self.get_append_right_fields_name(), rule, [])
        if append_right_fields:
            for right_field_name in append_right_fields:
                if right_field_name in right:
                    obj[right_field_name] = right[right_field_name]
        return obj

    def get_obj(self, operation=None, rule=None, left=None, right=None):
        """
        operation 操作 默认取rule 里面的，如果是新增和和删除，是可以传操作
        """
        if not operation:
            operation = self.get_operation()
        # 优先传过来的，如果没有则取配置里面的，再没有直接报错
        if not operation:
            return self.get_field() + "【" + self.get_operation_name() + "】字段不存在", False
        if not left:
            left = self.get_obj_left()
        if not right:
            right = self.get_obj_right()
        if not rule:
            rule = self.rule
        obj = self._get_obj(left, right, rule, operation=operation)
        return obj, True

    def get_true_value(self):
        return "True"

    def get_false_value(self):
        return "False"

    def hanlder_rule(self):
        return [], True


class FieldValueModifyRule(BaseModifyRule):
    """普通字段比较
            {

              "rule": "compare_field_value",
              "group": "server",
              "field": "server_ip",
              "operation": "modify",
              "desc": "普通字段比较，如果值相同则没有变化，template =True",
              "name": "服务器IP",
              "left": "",
              "right": "server_info",
              "template":"",
              "append_original_item": true,
              "append_right_fields": ["server_id"]
            }

    """

    def is_not_equal(self):
        templ = self.get_templ()
        # 获取左边对象
        left = self.get_obj_left()
        # 获取右边对象

        right = self.get_obj_right()
        # 如果配置template 则取template
        result = self.get_true_value()
        # 如果有模板优先匹配模板，计算模板返回True和False
        if templ:
            data_dict = {
                self.get_left_name(): left,
                self.get_right_name(): right
            }
            result = self.render(templ, data_dict)
        else:
            # 如果没有模板直接匹配值
            if self.get_left_value() != self.get_right_value():
                result = self.get_false_value()

        return result != self.get_true_value()

    def hanlder_rule(self):
        left = self.get_obj_left()
        if not isinstance(left, dict):
            return self.get_field() + "左边对象不是字段对象:" + str(left), False
        right = self.get_obj_right()
        if not isinstance(right, dict):
            return self.get_field() + "右边对象不是字段对象:" + str(right), False

        if self.is_not_equal():  # 如果不相等，则直接返回计算的比较对象
            obj, success = self.get_obj()
            if not success:
                return obj, success
            return [obj], True

        return [], True


class ArrayAddDeleteModifyRule(BaseModifyRule):
    """数组的新增和删除"""

    def get_key_name(self):
        return "key"

    def get_item_field_name(self):
        return "item_field"

    def get_item_field(self):
        return get_safe_data(self.get_item_field_name(), self.rule)

    def get_key(self):
        key_templ = get_safe_data(self.get_key_name(), self.rule)
        return key_templ

    def get_obj(self, left, right, rule=None, operation=None, transfer_dict=None):
        """
        operation 操作 默认取rule 里面的，如果是新增和和删除，是可以传操作
        """
        if not operation:
            operation = self.get_operation()
        # 优先传过来的，如果没有则取配置里面的，再没有直接报错
        if not operation:
            return self.get_field() + "【" + self.get_operation_name() + "】字段不存在", False
        if operation == self.get_add_operation():
            right = {}
        elif operation == self.get_remove_operation():
            left = {}
        if not rule:
            rule = self.rule
        obj = self._get_obj(left, right, rule, operation=operation, transfer_dict=transfer_dict)
        return obj, True

    def hanlder_rule(self):
        key_templ = self.get_key()
        if not key_templ:
            return self.get_field() + "【" + self.get_key_name() + "】字段不存在"
        item_field = self.get_item_field()
        if not item_field:
            msg = self.get_field() + "【" + self.get_item_field_name() + "】字段不存在"
            return msg, False
        value_templ = self.get_value_templ()
        if not value_templ:
            msg = self.get_value_name() + "字段不存在"
            return self.fail(msg)

        left = self.get_obj_left()
        right = self.get_obj_right()
        right_dict = {}

        for item in right:
            p = {item_field: item}
            key = self.render(key_templ, p)
            right_dict[key] = item
        # 获取新增的
        add_list = []
        for item in left:
            p = {item_field: item}
            key = self.render(key_templ, p)
            if key not in right_dict:
                add_list.append(item)
        # 获取删除的
        left_dict = {}
        remove_list = []

        for item in left:
            p = {item_field: item}
            key = self.render(key_templ, p)
            left_dict[key] = item
        for item in right:
            p = {item_field: item}
            key = self.render(key_templ, p)
            if key not in left_dict:
                remove_list.append(item)

        result_list = []
        for item in add_list:
            obj, success = self.get_obj(item, None, operation=self.get_add_operation())
            if success:
                result_list.append(obj)
            else:
                return obj, success

        for item in remove_list:
            obj, success = self.get_obj(None, item, operation=self.get_remove_operation())
            if success:
                result_list.append(obj)
            else:
                return obj, success

        return result_list, True


class ArrayFieldModifyRule(ArrayAddDeleteModifyRule):
    """数组的字段的修改"""

    def get_left_value_name(self):
        return "left_value"

    def get_right_value_name(self):
        return "right_value"

    def get_left_array_item_name(self):
        return "left_array_item"

    def get_right_array_item_name(self):
        return "right_array_item"

    def get_fields_name(self):
        return "fields"

    def get_transfer_result(self, transfer, current_value_list):
        current_value_list_field = get_safe_data("current_value_list_field", transfer,
                                                 "current_value_list_field")
        p = {
            current_value_list_field: current_value_list
        }
        # 构造一个服务
        import copy
        service = self.get_node_service(copy.deepcopy(transfer), p, self.template)
        if not self.is_success(service):
            return service
        service = self.get_data(service)
        # 运行服务的结果

        service_result = self.get_service_result(service, self.template)
        return service_result
        # if not self.is_success(service_result):
        #     return service_result
        # data = self.get_data(service_result)

    def hanlder_rule(self):
        key_templ = key_templ = self.get_key()
        if not key_templ:
            return self.get_field() + "【" + self.get_key_name() + "】字段不存在"
        item_field = self.get_item_field()
        if not item_field:
            msg = self.get_field() + "【" + self.get_item_field_name() + "】字段不存在"
            return msg, False
        left_array_item_name = get_safe_data(self.get_left_array_item_name(), self.rule)
        if not left_array_item_name:
            msg = self.get_field() + "【" + self.get_left_array_item_name() + "】字段不存在"
            return msg, False
        right_array_item_name = get_safe_data(self.get_right_array_item_name(), self.rule)
        if not right_array_item_name:
            msg = self.get_field() + "【" + self.get_right_array_item_name() + "】字段不存在"
            return msg, False
        fields = get_safe_data(self.get_fields_name(), self.rule)
        if not fields:
            msg = self.get_field() + "【" + self.get_fields_name() + "】字段不存在"
            return msg, False
        for index, field in enumerate(fields):
            left_value_templ = get_safe_data(self.get_left_value_name(), field)
            right_value_templ = get_safe_data(self.get_right_value_name(), field)
            templ = get_safe_data(self.get_template_name(), field)
            # if not templ:
            #     msg = "第 " + str(index + 1) + "字段规则【" + self.get_template_name() + "】字段不存在"
            #     return self.fail(msg)
            name = get_safe_data(self.get_name_name(), field)
            if not name:
                msg = self.get_field() + "第 " + str(index + 1) + "字段规则【" + self.get_name_name() + "】字段不存在"
                return msg, False
            field = get_safe_data(self.get_field_name(), field)
            if not field:
                msg = self.get_field() + "第 " + str(index + 1) + "字段规则【" + self.get_field_name() + "】字段不存在"
                return msg, False

        left = self.get_obj_left()
        right = self.get_obj_right()
        # 获取删除的
        left_dict = {}
        right_common_list = []
        for item in left:
            p = {item_field: item}
            key = self.render(key_templ, p)
            left_dict[key] = item
        for item in right:
            p = {item_field: item}
            key = self.render(key_templ, p)
            if key in left_dict:
                right_common_list.append(item)

        right_dict = {}
        left_common_list = []
        for item in right:
            p = {item_field: item}
            key = self.render(key_templ, p)
            right_dict[key] = item
        for item in left:
            p = {item_field: item}
            key = self.render(key_templ, p)
            if key in right_dict:
                left_common_list.append(item)

        right_common_list.sort(key=lambda item: self.render(key_templ, {item_field: item}))
        left_common_list.sort(key=lambda item: self.render(key_templ, {item_field: item}))
        result_list = []
        common_list = zip(left_common_list, right_common_list)
        for field in fields:
            field_change_list = []
            if not self.is_enable_rule(field):
                continue
            # 先获取要改变的值列表
            for left_item, right_item in common_list:
                templ = get_safe_data(self.get_template_name(), field)
                field_name = get_safe_data(self.get_field_name(), field)
                value_templ = get_safe_data(self.get_value_name(), field)
                name = get_safe_data(self.get_name_name(), field)
                if templ:
                    p = {
                        left_array_item_name: left_item,
                        right_array_item_name: right_item
                    }
                    result = self.render(templ, p)
                else:
                    if get_safe_data(field_name, left_item) == get_safe_data(field_name, right_item):
                        result = self.get_true_value()
                    else:
                        result = self.get_false_value()
                if result != self.get_true_value():
                    field_change_list.append({
                        self.get_left_name(): left_item,
                        self.get_right_name(): right_item,
                        self.get_rule_name(): field,
                        self.get_operation_name(): self.get_modify_name()
                    })
                # 获取规则值列表
            current_value_list = []
            # 计算值属性
            for change_item in field_change_list:
                right_value = self.get_field_value(get_safe_data(self.get_right_name(), change_item), field)
                left_value = self.get_field_value(get_safe_data(self.get_left_name(), change_item), field)
                if right_value is not None or right_value != "":
                    current_value_list.append(right_value)
                if left_value is not None or left_value != "":
                    current_value_list.append(left_value)

            transfer = self.get_transfer(field)
            transfer_dict = None
            # 为数组生成转换字典
            if transfer and current_value_list:
                current_value_list = list(set(current_value_list))
                service_result = self.get_transfer_result(transfer, current_value_list)
                if not self.is_success(service_result):
                    continue

                data_dict = {}
                data = self.get_data(service_result)
                if data:
                    for data_item in data:
                        transfer_key = get_safe_data(self.get_key_name(), transfer)
                        transfer_value_templ = get_safe_data(self.get_value_name(), transfer)
                        data_dict[self.render(transfer_key, data_item)] = self.render(transfer_value_templ, data_item)
                transfer_dict = data_dict
            # 转换数据
            for change_item in field_change_list:
                change_item["transfer_dict"] = transfer_dict
                result_item, success = self.get_obj(**change_item)
                if success:
                    result_list.append(result_item)

        return result_list, True


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
        "append_original_item_name": "append_original_item",
        "append_right_fields_name": "append_right_fields",

    }

    def get_append_right_fields_name(self):
        return self.gmd_const["append_right_fields_name"]

    def get_append_original_item_name(self):
        return self.gmd_const["append_original_item_name"]

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

    def get_add_operation(self):
        return self.gmd_const["add_name"]

    def get_remove_operation(self):
        return self.gmd_const["remove_name"]

    data_json_dict = {}

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
        from collect.service_imp.common.filters.template_tool import TemplateTool
        tool = TemplateTool(self.op_user)
        for index, rule in enumerate(fields):

            rule_name = get_safe_data(self.get_rule_name(), rule)
            if not rule_name:
                return self.fail(data_json_path + "配置文件中第" + str(index + 1) + "条规则没有配置" + self.get_rule_name())
            result = None
            name = get_safe_data(self.get_name_name(), rule)
            if self.can_log(template):
                self.log("处理第【{index}】规则：{name}".format(index=(index + 1), name=name))
                self.log(rule)
            field = get_safe_data(self.get_field_name(), rule)
            if not field:
                msg = self.get_error_msg(field, name, index, self.get_field_name() + "字段不存在")
                return self.fail(msg)
            if not name:
                msg = self.get_error_msg(field, name, index, self.get_name_name() + "字段不存在")
                return self.fail(msg)
            # 如果规则不可用则，跳过
            if not self.is_enable(params_result, rule):
                continue

            left_name = get_safe_data(self.get_left_name(), rule)
            # # 必须传left
            # if not left_name:
            #     msg = self.get_error_msg(field, name, index, self.get_left_name() + "字段不存在")
            #     return self.fail(msg)
            # 必须传right
            right_name = get_safe_data(self.get_right_name(), rule)
            if not right_name:
                msg = self.get_error_msg(field, name, index, self.get_right_name() + "字段不存在")
                return self.fail(msg)

            if rule_name == 'compare_field_value':
                """
                 处理简单值比较
                """
                fieldRule = FieldValueModifyRule(params=params_result,
                                                 rule=rule,
                                                 left_save_field=left_save_field,
                                                 right_save_field=right_save_field,
                                                 template=template,
                                                 renderFunction=self.get_render_data,
                                                 tool=tool,
                                                 get_node_service=self.get_node_service,
                                                 get_service_result=self.get_service_result)
                r, success = fieldRule.hanlder_rule()
                result = self.success(r)
                # result = self.handler_compare_field_value(params_result, rule, left_save_field, right_save_field,
                #                                           template)
            elif rule_name == 'compare_array_add_delete':
                """
                处理数组的新增和删除
                """

                fieldRule = ArrayAddDeleteModifyRule(params=params_result,
                                                     rule=rule,
                                                     left_save_field=left_save_field,
                                                     right_save_field=right_save_field,
                                                     template=template,
                                                     renderFunction=self.get_render_data,
                                                     tool=tool,
                                                     get_node_service=self.get_node_service,
                                                     get_service_result=self.get_service_result)
                r, success = fieldRule.hanlder_rule()
                result = self.success(r)
                # result = self.handler_compare_array_add_delete(params_result, rule, left_save_field, right_save_field,
                #                                                template)
            elif rule_name == 'compare_array_modify':
                """
                处理数组中同一个值的变化
                """
                # result = self.handler_compare_array_modify(params_result, rule, left_save_field, right_save_field,
                #                                            template)

                fieldRule = ArrayFieldModifyRule(params=params_result,
                                                 rule=rule,
                                                 left_save_field=left_save_field,
                                                 right_save_field=right_save_field,
                                                 template=template,
                                                 renderFunction=self.get_render_data,
                                                 tool=tool,
                                                 get_node_service=self.get_node_service,
                                                 get_service_result=self.get_service_result)
                r, success = fieldRule.hanlder_rule()
                result = self.success(r)

            if not result:
                continue
            if not self.is_success(result):
                msg = self.get_error_msg(field, name, index, self.get_msg(result))
                return self.fail(msg)
            result_data = self.get_data(result)
            if result_data:
                result_list += result_data

        if self.can_log(template):
            self.log("规则处理完毕")
            self.log(result_list)
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
            # if not templ:
            #     msg = "第 " + str(index + 1) + "字段规则【" + self.get_template_name() + "】字段不存在"
            #     return self.fail(msg)
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
                templ = get_safe_data(self.get_template_name(), field)
                field_name = get_safe_data(self.get_field_name(), field)
                value_templ = get_safe_data(self.get_value_name(), field)
                name = get_safe_data(self.get_name_name(), field)
                if templ:
                    p = {
                        left_array_item_name: left_item,
                        right_array_item_name: right_item
                    }
                    # if not templ:
                    #     templ = field
                    result = self.render_data(templ, p)
                else:
                    if get_safe_data(field_name, left_item) == get_safe_data(field_name, right_item):
                        result = self.get_true_value()
                    else:
                        result = self.get_false_value()
                if result != self.get_true_value():
                    left_value = self.render_data(value_templ, left_item)
                    right_value = self.render_data(value_templ, right_item)
                    append_original_item = get_safe_data(self.get_append_original_item_name(), field, False)
                    # 处理左边的数据
                    obj_result = self.get_obj(left_save_field, right_save_field, left_value, right_value, rule,
                                              template, operation=self.get_modify_name(), name=name, field=field_name,
                                              append_original_item=append_original_item, original_data=left_item
                                              )
                    # 处理右边的数据

                    if not self.is_success(obj_result):
                        return obj_result
                    append_right_fields = get_safe_data(self.get_append_right_fields_name(), field, [])
                    result_data = self.get_data(obj_result)
                    if append_right_fields:
                        for right_field_name in append_right_fields:
                            if right_field_name in right_item:
                                result_data[right_field_name] = right_item[right_field_name]
                    result_list += [result_data]

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
            key = self.render_data(templ, p, tool)
            right_dict[key] = item
        # 获取新增的
        add_list = []
        for item in left:
            p = {item_field_name: item}
            key = self.render_data(templ, p, tool)
            if key not in right_dict:
                add_list.append(item)
        # 获取删除的
        left_dict = {}
        remove_list = []

        for item in left:
            p = {item_field_name: item}
            key = self.render_data(templ, p, tool)
            left_dict[key] = item
        for item in right:
            p = {item_field_name: item}
            key = self.render_data(templ, p, tool)
            if key not in left_dict:
                remove_list.append(item)

        append_original_item = get_safe_data(self.get_append_original_item_name(), rule, False)
        result_list = []
        for item in add_list:
            p = {item_field_name: item}
            left = self.render_data(value_templ, p, tool)
            obj_result = self.get_obj(left_save_field, right_save_field, left, "", rule, template,
                                      self.get_add_operation(), append_original_item=append_original_item,
                                      original_data=item)
            if not obj_result:
                return self.fail(obj_result)
            result_list.append(self.get_data(obj_result))

        for item in remove_list:
            p = {item_field_name: item}
            right = self.render_data(value_templ, p, tool)
            obj_result = self.get_obj(left_save_field, right_save_field, "", right, rule, template,
                                      self.get_remove_operation(), append_original_item=append_original_item,
                                      original_data=item)
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
        field = get_safe_data(self.get_field_name(), rule)
        # if not templ:
        #     # msg = self.get_template_name() + "字段不存在"
        #     # return self.fail(msg)
        #     templ = get_safe_data(self.get_field_name(), rule)
        from collect.service_imp.common.filters.template_tool import TemplateTool
        tool = TemplateTool(self.op_user)
        left = self.render_data(get_safe_data(self.get_left_name(), rule), params, tool)
        right = self.render_data(get_safe_data(self.get_right_name(), rule), params, tool)
        result = self.get_true_value()
        if templ:
            data_dict = {
                self.get_left_name(): left,
                self.get_right_name(): right,
            }
            # 计算结果
            result = self.get_render_data(templ, data_dict, tool)
        else:
            if left != right:
                result = self.get_false_value()
        result_list = []
        if result != self.get_true_value():
            append_original_item = get_safe_data(self.get_append_original_item_name(), rule, False)
            obj_result = self.get_obj(left_save_field, right_save_field, left, right, rule, template,
                                      append_original_item=append_original_item,
                                      original_data=params)
            if not self.is_success(obj_result):
                return obj_result
            append_right_fields = get_safe_data(self.get_append_right_fields_name(), rule, [])
            result_data = self.get_data(obj_result)
            if append_right_fields:
                for right_field_name in append_right_fields:
                    result_data[right_field_name] = self.render_data(right_field_name, params, tool)
            result_list = [result_data]
        return self.success(result_list)

    def get_obj(self, left_save_field, right_save_field, left, right, rule, template, operation=None, name=None,
                field=None, append_original_item=False, original_data=None):
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

            # 处理如果是删除，则左边没有值，不必从数据库查询，直接滞空
            if operation != self.get_remove_operation():
                left_result = transferValue(left)
                if not self.is_success(left_result):
                    return left_result
                left = self.get_data(left_result)
            else:
                left = ""
            if operation != self.get_add_operation():
                right_result = transferValue(right)
                if not self.is_success(right_result):
                    return right_result
                right = self.get_data(right_result)
            else:
                right = ""
        if not name:
            name = get_safe_data(self.get_name_name(), rule)
        obj = {
            self.get_operation_name(): operation,
            left_save_field: left,
            right_save_field: right,
            self.get_field_name(): field,
            self.get_name_name(): name
        }
        if append_original_item and original_data:
            obj = dict(original_data.items() + obj.items())
        # obj[self.get_transfer_name()] = transfer
        return self.success(obj)
