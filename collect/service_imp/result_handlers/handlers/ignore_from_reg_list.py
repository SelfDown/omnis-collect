# -*- coding: utf-8 -*-
"""
@Time: 2021/8/4 16:51
@Author: zzhang zzhang@.com
@File: value_arr.py
@desc:
"""
from collect.service_imp.common.filters.template_tool import TemplateTool
from collect.service_imp.result_handlers.result_handler import ResultHandler
from collect.utils.collect_utils import get_safe_data


class IgnoreFromRegList(ResultHandler):

    def get_from_name(self):
        return "from"
    def handler(self, result, config, template):
        params = self.get_params_result(template)
        data = []
        from_reg_list_name = get_safe_data(self.get_from_name(),config)

        if not from_reg_list_name:
            return self.fail("结果正则过滤器，没有配置"+self.get_from_name())
        field_name = get_safe_data(self.get_field_name(), config)
        if not field_name:
            return self.fail("结果正则过滤器，没有配置"+self.get_field_name())
        reg_list = get_safe_data(from_reg_list_name,params)

        for data_item in result:
            value = get_safe_data(field_name,data_item,"")
            for reg_item in reg_list:
                import re
                r = re.findall(reg_item,value)
                if len(r)<=0:
                    data.append(data_item)

        return self.success(data)
