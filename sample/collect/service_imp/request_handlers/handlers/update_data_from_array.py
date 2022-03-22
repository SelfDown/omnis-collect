# -*- coding: utf-8 -*-
"""
@Time: 2021/8/8 8:47
@Author: zzhang zzhang@cenboomh.com
@File: prop_arr.py
@desc:
"""
from collect.service_imp.common.filters.template_tool import TemplateTool
from collect.service_imp.request_handlers.request_handler import RequestHandler
from collect.utils.collect_utils import get_safe_data


class UpdateDataFromArray(RequestHandler):
    udfaConst = {
        "item_name": "item",
        "fields_name": "fields",
        "from_list_name": "from_list",
        "from_item_name": "from_item",
        "second_item_name": "second_item",
        "ifTemplate_name": "ifTemplate",
    }

    def get_item_name(self):
        return self.udfaConst["item_name"]

    def get_fields_name(self):
        return self.udfaConst["fields_name"]

    def get_from_list_name(self):
        return self.udfaConst["from_list_name"]

    def get_second_item_name(self):
        return self.udfaConst["second_item_name"]

    def get_from_item_name(self):
        return self.udfaConst["from_item_name"]

    def get_ifTemplate_name(self):
        return self.udfaConst["ifTemplate_name"]

    def handler(self, params, config, template):
        config_params = get_safe_data(self.get_params_name(), config)

        if not config_params:
            return self.fail("更新数据处理器没有找到 {params} 节点".format(params=self.get_params_name()))

        template_tool = TemplateTool(op_user=self.op_user)
        foreach_name = get_safe_data(self.get_foreach_name(), config_params)
        if not foreach_name:
            return self.fail(self.get_foreach_name() + "字段配置没有找到")
        item_name = get_safe_data(self.get_item_name(), config_params)
        if not item_name:
            return self.fail(self.get_item_name() + "字段配置没有找到")
        foreach = get_safe_data(foreach_name, params)
        if not foreach:
            return self.fail(foreach_name + "字段参数没有找到")
        fields = get_safe_data(self.get_fields_name(), config_params)
        if not fields:
            return self.fail(self.get_fields_name() + "字段配置没有找到")

        fromListName = get_safe_data(self.get_from_list_name(), config_params)
        if not fromListName:
            return self.fail(self.get_from_list_name() + "字段配置没有找到")

        arr = fromListName.split(".")
        fromList = params[arr[0]]
        if len(arr) >= 2:
            secondArrName = arr[1]
            secondItemName = get_safe_data(self.get_second_item_name(), config_params)
            if not secondItemName:
                return self.fail(self.get_second_item_name() + "字段配置没有找到")
        else:
            secondArrName = None

        if not fromList:
            return self.fail("数组更新数据数组" + fromListName + "中" + t + "不存在")
        if not isinstance(fromList, list):
            return self.fail(fromListName + "不是数组对象")

        from_item_name = get_safe_data(self.get_from_item_name(), config_params)
        if not from_item_name:
            return self.fail(self.get_from_item_name() + "字段配置没有找到")

        ifTemplate = get_safe_data(self.get_ifTemplate_name(), config_params)
        if not ifTemplate:  #
            return self.fail("数组更新数据数组没有配置" + self.get_ifTemplate_name())
        import copy
        params_copy = copy.deepcopy(params)

        def update_fields(item, params_copy, template_tool, mustFieldsTemplate=False):
            # 批量更新字段
            for field in fields:
                # 判断是否需要根据字段，修改值
                fieldsIfTemplate = get_safe_data(self.get_ifTemplate_name(), field)
                if mustFieldsTemplate and not fieldsIfTemplate:
                    return self.fail(
                        get_safe_data(self.get_field_name(), field) + "字段没有配置" + self.get_ifTemplate_name())
                if fieldsIfTemplate:
                    ifValue = self.get_render_data(fieldsIfTemplate, params_copy, template_tool)
                    if ifValue != self.get_true_value():
                        continue

                temp = get_safe_data(self.get_template_name(), field)
                if not temp:
                    return self.fail(self.get_fields_name() + "没有配置" + self.get_template_name())
                field_name = get_safe_data(self.get_field_name(), field)
                item[field_name] = self.get_render_data(temp, params_copy, template_tool)
            return self.success([])

        for item in foreach:  # 数据源
            params_copy[item_name] = item
            for fromItem in fromList:  # 匹配列表

                params_copy[from_item_name] = fromItem
                ifValue = self.get_render_data(ifTemplate, params_copy, template_tool)
                if ifValue != self.get_true_value():
                    continue
                if secondArrName:
                    second_arr = get_safe_data(secondArrName, fromItem, [])
                    for second_item in second_arr:
                        params_copy[self.get_second_item_name()] = second_item
                        result = update_fields(item, params_copy, template_tool, True)
                        if not self.is_success(result):
                            return result
                else:
                    result = update_fields(item, params_copy, template_tool, False)
                    if not self.is_success(result):
                        return result

        if self.can_log(template):
            self.log(params)

        return self.success(params)
