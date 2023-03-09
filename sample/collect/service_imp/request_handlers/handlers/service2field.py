# -*- coding: utf-8 -*-
"""
@Time: 2021/7/26 14:58
@Author: zzhang zzhang@cenboomh.com
@File: service2field.py
@desc:
"""

from collect.service_imp.request_handlers.request_handler import RequestHandler
from collect.utils.collect_utils import get_safe_data


class Service2Field(RequestHandler):
    def get_append_param_name(self):
        return "append_param"
    def get_append_item_param_name(self):
        return "append_item_param"
    def get_append_item_match_name(self):
        return "append_item_match"
    def get_item_remove_prefix_name(self):
        return "item_remove_prefix"
    def handler(self, params, config, template):
        append_param = get_safe_data(self.get_append_param_name(),config)
        append_item_param_name = get_safe_data(self.get_append_item_param_name(),config)
        service_data = self.get_node_service(node=config, params=params, template=template, append_param=append_param)
        if not self.is_success(service_data):
            return service_data
        service = self.get_data(service_data)
        if append_item_param_name:
            append_item_param = get_safe_data(append_item_param_name,params)

            if not append_item_param:
                return self.fail("service2field没有找到参数"+append_item_param_name)
            append_param = get_safe_data(self.get_append_param_name(), config)
            # 获取匹配规则
            append_item_match = get_safe_data(self.get_append_item_match_name(), config)
            item_remove_prefix = get_safe_data(self.get_item_remove_prefix_name(), config)
            for key in append_item_param:
                # 如果字段不存在
                if  key  not in service:
                    param_value = append_item_param[key]
                    param_key = key
                    # 支持正则表达式
                    if append_item_match:
                        import re
                        if len(re.findall(append_item_match,key))<=0:
                            continue
                    # 支持替换前缀
                    if item_remove_prefix:
                        param_key = param_key.replace(item_remove_prefix,"")
                    service[param_key]= param_value
        service_result = self.get_service_result(service, template)
        if not self.is_success(service_result):
            self.log(self.get_msg(service_result), template=template)
            self.log(config, template=template)
            return service_result
        save_field = get_safe_data(self.get_save_field_name(), config)
        if save_field:
            params[save_field] = self.get_data(service_result)

        # result_template = get_safe_data(self.get_template_name(), config)
        # err_msg = get_safe_data(self.get_err_msg_name(), config)
        # if result_template:
        #     from collect.service_imp.common.filters.template_tool import TemplateTool
        #     template_tool = TemplateTool(op_user=self.op_user)
        #     check = template_tool.render(result_template, params)
        #     if check != self.get_true_value():
        #         return self.fail(err_msg)

        return self.success(params)
