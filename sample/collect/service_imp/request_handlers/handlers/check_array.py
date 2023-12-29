# -*- coding: utf-8 -*-
"""
@Time: 2021/7/26 15:31
@Author: zzhang zzhang@cenboomh.com
@File: updateData.py
@desc:
"""
from collect.service_imp.common.filters.template_tool import TemplateTool
from collect.service_imp.request_handlers.request_handler import RequestHandler
from collect.utils.collect_utils import get_safe_data


class CheckArray(RequestHandler):
    CAConst = {
        "fields_name": "fields",
        "item_name": "item",
        "item_order_index_name": "item_order_index"

    }

    def get_item_order_index_name(self):
        return self.CAConst["item_order_index_name"]

    def get_fields_name(self):
        return self.CAConst["fields_name"]

    def get_item_name(self):
        return self.CAConst["item_name"]

    def handler(self, params, config, template):

        template_tool = TemplateTool(op_user=self.op_user)
        foreach_name = get_safe_data(self.get_foreach_name(), config)
        if not foreach_name:
            return self.fail(self.get_foreach_name() + "字段配置没有找到")
        item_name = get_safe_data(self.get_item_name(), config)
        if not item_name:
            return self.fail(self.get_item_name() + "字段配置没有找到")
        foreach = self.render_data(foreach_name, params)
        if not foreach:
            return self.fail(foreach_name + "字段参数没有找到")
        fields = get_safe_data(self.get_fields_name(), config)
        if not fields:
            return self.fail(self.get_fields_name() + "字段配置没有找到")
        import copy
        params_copy = copy.deepcopy(params)
        for item_order_index, item in enumerate(foreach):
            params_copy[item_name] = item
            params_copy[self.get_item_order_index_name()] = item_order_index + 1
            for field_index, field in enumerate(fields):
                temp = get_safe_data(self.get_template_name(), field)
                if not temp:
                    return self.fail(" 第 【" + str(field_index + 1) + "】 没有配置" + self.get_template_name())
                err_msg = get_safe_data(self.get_err_msg_name(), field)
                if not err_msg:
                    return self.fail(" 第 【" + str(field_index + 1) + "】 没有配置" + self.get_err_msg_name())
                success = self.get_render_data(temp, params_copy, template_tool)
                if success == self.get_false_value():
                    err = self.get_render_data(err_msg, params_copy, template_tool)
                    return self.fail(err)

        return self.success(params)
