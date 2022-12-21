# -*- coding: utf-8 -*-
"""
@Time: 2021/8/2 16:52
@Author: zzhang zzhang@cenboomh.com
@File:
@desc:
"""
from collect.service_imp.flow.collect_flow import ServiceCollectFlowService
from collect.utils.collect_utils import get_safe_data, get_key


class ServiceFlowService(ServiceCollectFlowService):
    sf_const = {
        "flow_name": "flow",
        "strict_name": "strict",
    }

    def get_flow_name(self):
        return self.sf_const["flow_name"]

    def get_strict_name(self):
        return self.sf_const["strict_name"]

    data_json_dict = {}

    @staticmethod
    def get_json_content(path):
        return get_safe_data(path, ServiceFlowService.data_json_dict)

    @staticmethod
    def set_json_content(path, data_json_content):
        ServiceFlowService.data_json_dict[path] = data_json_content

    def get_flow(self):
        if get_safe_data(self.get_data_json_name(), self.template):
            data_json_result = self.get_data_json(self.get_params_result())
            if not self.is_success(data_json_result):
                return data_json_result
            data_json = self.get_data(data_json_result)
            import json
            data_json = json.loads(data_json)
            return data_json
        return get_safe_data(self.get_flow_name(), self.template)

    def handler_current_node(self, current):
        params_result = self.get_params_result()
        strict = get_safe_data(self.get_strict_name(), current, False)
        append_param = not strict
        # service = get_safe_data(self.get_service_name(), current)
        from collect.service_imp.common.filters.template_tool import TemplateTool

        template_tool = TemplateTool(op_user=self.op_user)
        import copy
        node = copy.deepcopy(current)
        service = self.get_node_service(node, params_result, template_tool, append_param=append_param,
                                        nullToTemplateField=False)
        # service = self.get_node_service(current, params_result, template_tool, append_param=append_param,
        #                                 nullToTemplateField=False)
        if not self.is_success(service):
            return service
        service = self.get_data(service)
        service_result = self.get_service_result(service, self.template)
        if not self.is_success(service_result):
            return service_result
        data = self.get_data(service_result)
        return self.success(data)

    def execute(self, handler_node):
        self.set_flow(self.get_flow())
        # 必须包含service 节点
        self.set_must_node_names([self.get_service_name()])
        self.set_flow_name(self.get_flow_name())
        flow_result = self.flow(handler_node)
        return flow_result

    def result(self, params):
        flow = self.get_flow()
        if not flow:
            return self.fail(msg="没有找到" + self.get_flow_name() + "节点，请检查配置")
        flow_result = self.execute(self.handler_current_node)
        if not self.is_success(flow_result):
            return flow_result
        return self.success({})
