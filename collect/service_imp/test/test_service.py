# -*- coding: utf-8 -*-
"""
@Time: 2021/7/14 16:32
@Author: zzhang zzhang@cenboomh.com
@File: ModelUpdate.py
@desc:
"""
from collect.collect_service import CollectService
from collect.utils.collect_utils import get_safe_data


class TestService(CollectService):
    data_json_dict = {}
    HConst = {
        "data_json_name": "data_json",
        "success_name": "success",
    }

    def __init__(self, op_user):
        CollectService.__init__(self, op_user)
        pass

    def get_success_name(self):
        return self.HConst["success_name"]

    def get_data_json_name(self):
        return self.HConst["data_json_name"]

    @staticmethod
    def get_json_content(path):
        return get_safe_data(path, TestService.data_json_dict)

    @staticmethod
    def set_json_content(path, data_json_content):
        TestService.data_json_dict[path] = data_json_content

    def get_data_json_config_path(self):
        data_json = get_safe_data(self.get_data_json_name(), self.template)
        config_dir = self.get_config_dir()
        config_file = config_dir + "/" + data_json
        return config_file

    def get_data_json(self, params):
        config_file_path = self.get_data_json_config_path()
        json_content = self.get_json_content(config_file_path)
        if json_content:
            return self.success(json_content)
        data_json = get_safe_data(self.get_data_json_name(), self.template)
        data_json_result = self.get_config_file(data_json, params)
        if self.is_success(data_json_result):
            data_json_content = self.get_data(data_json_result)
            self.set_json_content(config_file_path, data_json_content)
        return data_json_result

    def result(self, params=None):
        return self.success(params)
