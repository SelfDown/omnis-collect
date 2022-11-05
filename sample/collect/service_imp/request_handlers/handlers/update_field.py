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


class UpdateField(RequestHandler):
    UFConst = {
        "fields_name": "fields",

    }

    def get_fields_name(self):
        return self.UFConst["fields_name"]

    def handler(self, params, config, template):

        template_tool = TemplateTool(op_user=self.op_user)
        fields = get_safe_data(self.get_fields_name(), config)
        if not fields:
            return self.fail(self.get_fields_name() + "字段配置没有找到")
        params_result = self.get_params_result(template)
        for field in fields:
            temp = get_safe_data(self.get_template_name(), field)
            if not temp:
                return self.fail(self.get_fields_name() + "没有配置" + self.get_template_name())
            if not self.is_enable(params_result, field):
                continue
            field_name = get_safe_data(self.get_field_name(), field)
            params_result[field_name] = self.get_render_data(temp, params_result, template_tool)

        if self.can_log(template):
            self.log(params, template=template)
        return self.success(params)
