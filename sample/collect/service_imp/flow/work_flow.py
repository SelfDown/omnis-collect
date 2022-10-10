# -*- coding: utf-8 -*-
"""
@Time: 2021/8/2 16:52
@Author: zzhang zzhang@cenboomh.com
@File:
@desc:
"""
from collect.service_imp.flow.collect_flow import ServiceCollectFlowService
from collect.utils.collect_utils import get_safe_data, get_key


class WorkFlowService(ServiceCollectFlowService):
    wf_const = {
        "flow_name": "flow",
        "strict_name": "strict",
        "services_name": "services",
        "status_field_name": "status_field",
        "only_flow_name": "only_flow",

    }

    data_json_dict = {}

    @staticmethod
    def get_json_content(path):
        return get_safe_data(path, WorkFlowService.data_json_dict)

    @staticmethod
    def set_json_content(path, data_json_content):
        WorkFlowService.data_json_dict[path] = data_json_content

    def get_flow_name(self):
        return self.wf_const["flow_name"]

    def get_status_field_name(self):
        return self.wf_const["status_field_name"]

    def get_services_name(self):
        return self.wf_const["services_name"]

    def get_strict_name(self):
        return self.wf_const["strict_name"]

    def get_only_flow_name(self):
        return self.wf_const["only_flow_name"]

    def get_flow(self):
        return get_safe_data(self.get_flow_name(), self.template)

    def handler_current_node(self, current):
        params_result = self.get_params_result()
        strict = get_safe_data(self.get_strict_name(), current, False)
        append_param = not strict
        # service = get_safe_data(self.get_service_name(), current)
        from collect.service_imp.common.filters.template_tool import TemplateTool

        template_tool = TemplateTool(op_user=self.op_user)
        service = self.get_node_service(current, params_result, template_tool, append_param=append_param,
                                        nullToTemplateField=False)
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

        params_result = self.get_params_result()
        data_json_result = self.get_data_json(params_result)
        if not self.is_success(data_json_result):
            return data_json_result
        data_json = self.get_data(data_json_result)
        import json
        data_json = json.loads(data_json)
        flow = get_safe_data(self.get_flow_name(), data_json)
        if not flow:
            return self.fail(msg="没有找到" + self.get_flow_name() + "节点，请检查配置")
        services = get_safe_data(self.get_services_name(), flow)
        only_flow_templ = get_safe_data(self.get_only_flow_name(), self.template)
        only_flow = self.render_data(only_flow_templ, params_result)
        if only_flow == self.get_true_value() or only_flow == True:
            return self.success(services)
        service_dict_result = self.get_service_dict(services)
        if not self.is_success(service_dict_result):
            return service_dict_result
        service_dict = self.get_data(service_dict_result)
        status_name = get_safe_data(self.get_status_field_name(), self.template)
        if not status_name:
            return self.fail("没有配置" + self.get_status_field_name())
        status = get_safe_data(status_name, params_result)
        node = get_safe_data(status, service_dict)
        if not node:
            return self.fail("工作流没有找打节点【" + status + "】")
        node_type = get_safe_data(self.get_type_name(), node)
        if self.get_end_name() == node_type:
            return self.success([], msg="流程已经结束")
        next = get_safe_data(self.get_next_name(), node)
        node_list = []
        for node_item in next:
            node_list.append(get_safe_data(node_item, service_dict))
        return self.success(node_list)
