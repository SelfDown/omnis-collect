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


class NewField(RequestHandler):
    NFConst = {
        "fields_name": "fields"
    }

    def get_fields_name(self):
        return self.NFConst["fields_name"]

    def handler(self, params, config, template):
        fields = get_safe_data(self.get_fields_name(), config)
        if not fields:
            return self.fail(self.get_fields_name() + "字段配置没有找到")
        params_result = self.get_params_result(template)
        template_tool = TemplateTool(op_user=self.op_user)
        for field in fields:
            key = get_safe_data(self.get_key_name(), field)
            if not key:
                continue
            templ = get_safe_data(self.get_template_name(), field, "")
            value = self.get_render_data(templ, params_result, template_tool)
            params[key] = value
        if self.can_log(template):
            self.log(params,template=template)
        return self.success(params)
