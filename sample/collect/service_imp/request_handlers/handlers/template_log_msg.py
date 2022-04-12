# -*- coding: utf-8 -*-
"""
@Time: 2021/7/26 15:31
@Author: zzhang zzhang@cenboomh.com
@File: updateData.py
@desc:
"""
from collect.service_imp.common.filters.template_tool import TemplateTool
from collect.service_imp.request_handlers.request_handler import RequestHandler
from collect.utils.collect_utils import get_safe_data, DateEncoder


class TemplateLogMsg(RequestHandler):
    TLMConst = {
        "data_list_name": "data_list",
        "msg_name": "msg",
        "data_name": "data"
    }

    def get_data_list_name(self):
        return self.TLMConst["data_list_name"]

    def get_data_name(self):
        return self.TLMConst["data_name"]

    def get_msg_name(self):
        return self.TLMConst["msg_name"]

    def handler(self, params, config, template):
        data_list = get_safe_data(self.get_data_list_name(), params)
        if not data_list:
            return self.fail(self.get_data_list_name() + "字段参数没有找到")
        save_field = get_safe_data(self.get_save_field_name(), config)
        if not save_field:
            return self.fail(self.get_save_field_name() + "字段配置没有找到")
        config_type = get_safe_data(self.get_type_name(), config)
        if not config_type:
            return self.fail(self.get_type_name() + "字段配置没有找到")
        result_list = []
        for item in data_list:
            msg_type = get_safe_data(self.get_type_name(), item)
            # 匹配类型
            if config_type == msg_type:
                # todo 处理显示密码
                msg_name = self.get_msg_name()

                data_name = self.get_data_name()
                if data_name in item:
                    data_item = item[data_name]
                    if msg_name in data_item and (
                            isinstance(data_item[msg_name], dict) or isinstance(data_item[msg_name], list)):
                        import json
                        data_item[msg_name] = json.dumps(data_item[msg_name], cls=DateEncoder, ensure_ascii=False)
                    result_list.append(data_item)
        params[save_field] = result_list
        return self.success(params)
