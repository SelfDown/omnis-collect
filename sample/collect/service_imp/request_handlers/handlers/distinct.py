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


class Distinct(RequestHandler):

    def get_fields_name(self):
        return "fields"

    def handler(self, params, config, template):
        fields = get_safe_data(self.get_fields_name(), config)
        if not fields:
            return self.fail("没有找到" + self.get_fields_name())
        foreach_name = get_safe_data(self.get_foreach_name(), config)
        if not foreach_name:
            return self.fail("没有找到" + self.get_foreach_name())
        key_list = []
        foreach = params[foreach_name]

        def get_key(data_item):
            l = []
            for item in fields:
                value = get_safe_data(item["field"], data_item)
                if value is None:
                    value = ""
                l.append(value)
            return "#".join(l)

        result_list = []
        for data_item in foreach:
            key = get_key(data_item)
            if key not in key_list:
                key_list.append(key)
                result_list.append(data_item)
        save_field = get_safe_data(self.get_save_field_name(), config)
        if save_field:
            params[save_field] = result_list
        return self.success(params)
