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


class FilterArr(RequestHandler):
    faConst = {
        "ifTemplateName": "ifTemplate",
        "item_name": "item"
    }

    def getIfTemplateName(self):
        return self.faConst["ifTemplateName"]

    def get_item_name(self):
        return self.faConst["item_name"]

    def handler(self, params, config, template):

        foreach_name = get_safe_data(self.get_foreach_name(), config)

        if not foreach_name:
            return self.fail("过滤数组有找到 {params} 节点".format(params=self.get_foreach_name()))
        ifTemplate = get_safe_data(self.getIfTemplateName(), config)
        if not ifTemplate:
            return self.fail("过滤数组处理器 {params} 节点".format(params=self.getIfTemplateName(), ))
        save_field = get_safe_data(self.get_save_field_name(), config)

        foreach = get_safe_data(foreach_name, params)
        if not isinstance(foreach, list):
            return self.success(params)
        result_list = []
        tool = TemplateTool(op_user=self.op_user)
        item_name = get_safe_data(self.get_item_name(), config, "item")

        for item in foreach:
            val = self.get_render_data(ifTemplate, {item_name: item}, tool)
            if val != self.get_true_value():
                continue
            result_list.append(item)

        params[save_field] = result_list

        return self.success(params)
