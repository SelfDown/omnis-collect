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


class Max(RequestHandler):

    def get_reg_name(self):
        return "reg"

    def handler(self, params, config, template):
        foreach_name = get_safe_data(self.get_foreach_name(), config)
        if not foreach_name:
            return self.fail("没有找到foreach ，在max中")
        foreach = self.render_data(foreach_name, params)
        field_name = get_safe_data(self.get_field_name(), config)
        max_value = None
        max_value_item = None
        for item in foreach:
            value = self.render_data(field_name, item)
            if not value:
                continue
            if not max_value or value > max_value:  # 如果之前没有赋值过则赋值
                max_value_item = item
                max_value = value

        save_field = get_safe_data(self.get_save_field_name(), config)
        if save_field and max_value_item:
            params[save_field] = max_value_item
        return self.success(params)
