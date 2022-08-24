# -*- coding: utf-8 -*-

from collect.service_imp.request_handlers.request_handler import RequestHandler
from collect.utils.collect_utils import get_safe_data


class arrayValue(RequestHandler):
    """
     从数组中，取值
    """
    av_const = {
        "foreach_name": "foreach",
        "ifTemplate_name": "ifTemplate",
        "valueTemplate_name": "valueTemplate",
        "item_name": "item",
    }

    def get_item_name(self):
        return self.av_const["item_name"]

    def get_foreach_name(self):
        return self.av_const["foreach_name"]

    def get_if_template_name(self):
        return self.av_const["ifTemplate_name"]

    def get_value_template_name(self):
        return self.av_const["valueTemplate_name"]

    def handler(self, params, config, template):
        foreach_name = get_safe_data(self.get_foreach_name(), config)
        if not foreach_name:
            return self.fail("arrayValue 转换器"+self.get_foreach_name() + "字段配置不存在")
        arr = foreach_name.split(".")
        foreach = params
        for name in arr:
            if name not in foreach:
                return self.fail("arrayValue 转换器"+name + "字段数据不存在")
            foreach = foreach[name]
        if not isinstance(foreach, list):
            return self.fail(msg="arrayValue 转换器"+name+"循环对象非数组")
        save_field = get_safe_data(self.get_save_field_name(), config)
        if not save_field:
            return self.fail(msg="arrayValue 转换器"+self.get_save_field_name() + "字段不存在")
        if len(foreach) <= 0:
            params[save_field] = ""
            return self.success(params)
        ifTemplate_name = get_safe_data(self.get_if_template_name(), config)
        if not ifTemplate_name:
            return self.fail("arrayValue 转换器"+self.get_if_template_name() + "不能为空")

        valueTemplate = get_safe_data(self.get_value_template_name(), config)
        if not valueTemplate:
            return self.fail("arrayValue 转换器"+self.get_value_template_name() + "不能为空")

        from collect.service_imp.common.filters.template_tool import TemplateTool
        tool = TemplateTool(op_user=self.op_user)
        for item in foreach:
            t = dict(params.items()+{self.get_item_name(): item}.items() )
            v = self.get_render_data(ifTemplate_name, t, tool)
            if v == self.get_true_value():
                value = self.get_render_data(valueTemplate, t, tool)
                params[save_field] = value
                break

        return self.success(params)
