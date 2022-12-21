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


class PropArr(RequestHandler):
    paConst = {
        "unique_name": "unique"
    }
    def get_sub_field_name(self):
        return "sub_field"

    def get_unique_name(self):
        return self.paConst["unique_name"]

    def handler(self, params, config, template):

        config_params = get_safe_data(self.get_params_name(), config)

        if not config_params:
            return self.fail("值列表处理器没有找到 {params} 节点".format(params=self.get_params_name()))
        from_field = get_safe_data(self.get_from_field_name(), config_params)
        if not from_field:
            return self.fail("值列表处理器 {params} 节点,没有找到{from_field}".format(params=self.get_params_name(),
                                                                          from_field=self.get_from_field_name()))
        to_field = get_safe_data(self.get_to_field_name(), config_params)
        if not to_field:
            return self.fail("值列表处理器 {params} 节点,没有找到{to_field}".format(params=self.get_params_name(),
                                                                        to_field=self.get_to_field_name()))
        templ = get_safe_data(self.get_template_name(), config_params)
        if not to_field:
            return self.fail("值列表处理器 {params} 节点,没有找到{template}".format(params=self.get_params_name(),
                                                                        template=self.get_template_name()))
        from_list = get_safe_data(from_field, params)
        if not isinstance(from_list, list):
            return self.fail("值列表处理器 请求参数" + from_field + " 不是数组")
        unique = get_safe_data(self.get_unique_name(), config_params)
        sub_field_name = get_safe_data(self.get_sub_field_name(),config_params)
        result_list = []
        tool = TemplateTool(op_user=self.op_user)

        def add_val(param):
            if not param:
                return
            val = self.get_render_data(templ, param, tool)
            if not val:
                return
            if unique and val in result_list:
                return
            result_list.append(val)

        for item in from_list:
            # 如是简单数组
            if not sub_field_name:
                add_val(item)
                continue
            # 处理二级数组
            sub_list = get_safe_data(sub_field_name,item,[])
            for sub_item in sub_list:
                add_val(sub_item)

        params[to_field] = result_list

        return self.success(params)
