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


class RegField(RequestHandler):

    def get_reg_name(self):
        return "reg"

    def handler(self, params, config, template):
        field_name = self.render_data(self.get_field_name(), config)
        field = self.render_data(field_name, params)
        import re
        reg = get_safe_data(self.get_reg_name(),config)
        d = re.match(reg, field).groups()
        save_field = get_safe_data(self.get_save_field_name(), config)
        if save_field:
            if len(d) > 0:
                params[save_field] = d[0]
            else:
                params[save_field]=""

        if self.can_log(template):
            self.log(params, template=template)
        return self.success(params)
