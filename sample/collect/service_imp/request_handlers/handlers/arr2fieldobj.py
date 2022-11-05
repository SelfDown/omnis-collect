# -*- coding: utf-8 -*-
"""
@Time: 2021/8/26 14:58
@Author: zzhang zzhang@cenboomh.com
@File: arr2arrobj.py
@desc:
"""
from collect.service_imp.request_handlers.request_handler import RequestHandler
from collect.utils.collect_utils import get_safe_data


class Arr2FieldObj(RequestHandler):
    """
    数组列表，转数组对象
    """
    afo_const = {
        "fields_name": "fields",
        "item_name": "item",
    }

    def get_fields_name(self):
        return self.afo_const["fields_name"]

    def get_item_name(self):
        return self.afo_const["item_name"]

    def handler(self, params, config, template):
        foreach_name = get_safe_data(self.get_foreach_name(), config)
        if not foreach_name:
            return self.fail(self.get_foreach_name() + "字段配置不存在")

        foreach = get_safe_data(foreach_name, params)
        if not foreach:
            return self.fail(self.get_foreach_name() + "不能为空")

        save_field_name = get_safe_data(self.get_save_field_name(), config)
        if not save_field_name:
            return self.fail(self.get_save_field_name() + "字段配置不存在")

        fields = get_safe_data(self.get_fields_name(), config)
        if not fields:
            return self.fail(self.get_fields_name() + "字段配置不存在")
        from collect.service_imp.common.filters.template_tool import TemplateTool
        tool = TemplateTool(op_user=self.op_user)
        l = {}

        for item in foreach:
            t = dict(self.get_params_result(template).items() + {self.get_item_name(): item}.items())
            for field in fields:
                name_tpl = get_safe_data(self.get_field_name(), field)
                value_tpl = get_safe_data(self.get_value_name(), field)
                name = self.get_render_data(name_tpl, t, tool)
                value = self.get_render_data(value_tpl, t, tool)
                l[name] = value

        params[save_field_name] = l
        return self.success(params)
