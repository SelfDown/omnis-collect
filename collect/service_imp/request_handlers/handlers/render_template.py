# -*- coding: utf-8 -*-
import json

from collect.service_imp.request_handlers.request_handler import RequestHandler
from collect.utils.collect_utils import get_safe_data


class RenderTemplate(RequestHandler):
    """
     生成内容
    """
    rt_const = {
        "template_file_name": "template_file"
    }

    def get_template_file_name(self):
        return self.rt_const["template_file_name"]

    data_json_dict = {}

    @staticmethod
    def get_json_content(path):
        return get_safe_data(path, RenderTemplate.data_json_dict)

    @staticmethod
    def set_json_content(path, data_json_content):
        RenderTemplate.data_json_dict[path] = data_json_content

    def handler(self, params, config, template):
        data_json_path = get_safe_data(self.get_template_file_name(), config)
        if not data_json_path:
            return self.fail(self.get_data_json_name() + "字段不存在")
        templ = self.get_data_json(params, data_json_path, template)
        if not self.is_success(templ):
            return templ
        templ = self.get_data(templ)
        params_result = self.get_params_result(template)
        if self.can_log(template):
            self.log(templ, template)
            self.log(params_result, template)

        from collect.service_imp.common.filters.template_tool import TemplateTool
        tool = TemplateTool(self.op_user)
        value = self.get_render_data(templ=templ, tool=tool, params=params_result)
        if self.can_log(template):
            self.log("渲染结果", template)
            self.log(value, template)
        save_field = get_safe_data(self.get_save_field_name(), config)
        if save_field:
            params[save_field] = value
        return self.success(params)

    # def handler(self, params, config, template):
    #     # 根据template_file 生成模板
    #     session_key_name = get_safe_data(self.get_session_key_name(), config)
    #     if not session_key_name:
    #         return self.fail(self.get_session_key_name() + "字段不存在")
    #     session = self.get_session(template)
    #     value = get_safe_data(session_key_name, session)
    #     # 处理保存字段
    #     save_field = get_safe_data(self.get_save_field_name(), config)
    #     if save_field:
    #         params[save_field] = value
    #     return self.success(params)
