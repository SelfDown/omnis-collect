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


class Reg2List(RequestHandler):
    def get_reg_name(self):
        return "reg"

    def get_from_name(self):
        return "from"

    def get_fields(self):
        return "fields"

    def handler(self, params, config, template):
        reg = get_safe_data(self.get_reg_name(), config)
        from_name = get_safe_data(self.get_from_name(), config)
        fields = get_safe_data(self.get_fields(), config)
        save_field = get_safe_data(self.get_save_field_name(), config)
        content = get_safe_data(from_name, params)
        import re
        data_list = re.findall(reg, content)
        result_list = []
        for item in data_list:
            obj = {}
            for k, v in zip(fields, item):
                field = get_safe_data(self.get_field_name(), k)
                obj[field] = v
            result_list.append(obj)
        params[save_field] = result_list
        return self.success(params)
