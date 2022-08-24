# -*- coding: utf-8 -*-
"""
@Time: 2021/8/9 17:46
@Author: zzhang zzhang@cenboomh.com
@File: combine_service.py
@desc:
"""
from collect.service_imp.common.filters.template_tool import TemplateTool
from collect.service_imp.result_handlers.result_handler import ResultHandler
from collect.utils.collect_utils import get_safe_data


class CombineService(ResultHandler):
    cs_const = {
        "multiple_name": "multiple",
        "result_name": "result_name",
        "append_param_name":"append_param"
    }

    def get_append_param_name(self):
        return self.cs_const["append_param_name"]
    def get_result_name(self):
        return self.cs_const["result_name"]

    def get_multiple_name(self):
        return self.cs_const["multiple_name"]

    def handler(self, result, config, template):
        params = get_safe_data(self.get_params_name(), config)
        # 如果是空对象，直接返回
        if not result:
            return self.success(result)
        if not params:
            return self.fail("结合服务处理器没有找到 {params} 节点".format(params=self.get_params_name()))

        service = get_safe_data(self.get_service_name(), params)
        if not service:
            return self.fail(
                "结合服务处理器没有找到 {params} 节点 没有找到{field}".format(params=self.get_params_name(),
                                                             field=self.get_service_name()))

        from_field = get_safe_data(self.get_from_field_name(), params)
        if not from_field:
            return self.fail(
                "结合服务处理器没有找到 {params} 节点 没有找到{field}".format(params=self.get_params_name(),
                                                             field=self.get_from_field_name()))

        to_field = get_safe_data(self.get_to_field_name(), params)
        if not to_field:
            return self.fail(
                "结合服务处理器没有找到 {params} 节点 没有找到{field}".format(params=self.get_params_name(),
                                                             field=self.get_to_field_name()))

        save_field = get_safe_data(self.get_save_field_name(), params)
        if not save_field:
            return self.fail(
                "结合服务处理器没有找到 {params} 节点 没有找到{field}".format(params=self.get_params_name(),
                                                             field=self.get_save_field_name()))

        multiple = get_safe_data(self.get_multiple_name(), params)

        params_result = self.get_params_result(template)
        # 如果有设置结果参数，则设置结果
        result_name = get_safe_data(self.get_result_name(), params)
        if result_name:
            params_result[result_name] = result
        # 处理是否拼接其他参数，默认拼接所有参数
        append_param = True
        if self.get_append_param_name() in params:
            append_param = params[self.get_append_param_name()]
        s_result = self.get_node_service(params, params=params_result, template=template, append_param=append_param)
        if not self.is_success(s_result):
            return s_result
        service = self.get_data(s_result)
        service_result = self.get_service_result(service, template)
        if not self.is_success(service_result):
            return service_result
        service_result = self.get_data(service_result)
        if not service_result:
            service_result = []
        service_result_dict = {}
        for item in service_result:
            if from_field not in item:
                continue
            val_key = item[from_field]
            if multiple:
                if val_key not in service_result_dict:
                    service_result_dict[val_key] = []
                service_result_dict[val_key].append(item)
            else:
                service_result_dict[val_key] = item

        def handler_data(item):
            if to_field not in item:
                return
            val_key = item[to_field]
            if val_key not in service_result_dict:
                if not multiple:
                    item[save_field] = {}
                else:
                    item[save_field] = []
                return
            item[save_field] = service_result_dict[val_key]

        if isinstance(result, dict):
            handler_data(result)
        else:
            for item in result:
                handler_data(item)

        return self.success(result)
