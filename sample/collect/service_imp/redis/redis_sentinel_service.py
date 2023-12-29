# -*- coding: utf-8 -*-
"""
@Time: 2021/7/14 16:32
@Author: zzhang zzhang@cenboomh.com
@File: ModelUpdate.py
@desc:
"""
import json

from redis.sentinel import Sentinel

from collect.collect_service import CollectService
from collect.utils.collect_utils import get_safe_data
from ldap3 import Server, Connection, SUBTREE, ALL_ATTRIBUTES, ALL, MODIFY_ADD, MODIFY_REPLACE


class RedisSentinelService(CollectService):
    data_json_dict = {}
    LSConst = {
        "data_json_name": "data_json",
        "connection_name": "connection",
        "result_name": "result",
        "result_field_name": "result_field",
        "entries_first_name": "entries_first",
        "entries_all_name": "entries_all",
        "ignore_status_name": "ignore_status",
        "log_name": "log"

    }

    def get_ignore_status_name(self):
        return self.LSConst["ignore_status_name"]

    def get_entries_first_name(self):
        return self.LSConst["entries_first_name"]

    def get_entries_all_name(self):
        return self.LSConst["entries_all_name"]

    def get_result_field_name(self):
        return self.LSConst["result_field_name"]

    def get_result_name(self):
        return self.LSConst["result_name"]

    def get_redis_template(self):
        """
         获取配置的ldap 模板，必须之前 get_template_from_template
        """
        return self.redis_template

    def set_redis_template(self, redis_template):
        self.redis_template = redis_template

    def get_connection_name(self):
        return self.LSConst["connection_name"]

    def get_data_json_name(self):
        return self.LSConst["data_json_name"]

    @staticmethod
    def get_json_content(path):
        return get_safe_data(path, RedisSentinelService.data_json_dict)

    @staticmethod
    def set_json_content(path, data_json_content):
        RedisSentinelService.data_json_dict[path] = data_json_content

    def get_data_json_config_path(self):
        data_json = get_safe_data(self.get_data_json_name(), self.template)
        if not data_json:
            self.log("没有找到" + self.get_data_json_name() + "配置文件")
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

    def __init__(self, op_user):
        CollectService.__init__(self, op_user)
        self.MYSETINEL = None
        self.MASTER = None
        self.SLAVE = None
        self.redis_template = None

        pass

    def get_ldap_param(self, data_json_templ, params_result):
        from collect.service_imp.common.filters.template_tool import TemplateTool
        tool = TemplateTool(op_user=self.op_user)
        data_json = tool.render(data_json_templ, params_result)
        try:
            import json
            data_json = json.loads(data_json)
            return self.success(data_json)
        except Exception as e:
            self.log(data_json, "error")
            return self.fail(str(e) + " JSON格式有误，请检查配置")

    def get_connection_from_template(self):
        redis_template = self.get_redis_template()
        connection_dict = get_safe_data(self.get_connection_name(), redis_template)
        if not connection_dict:
            return self.fail("没有配置连接信息")

        try:
            MYSETINEL = Sentinel(**connection_dict["sentinel"])
            # 通过哨兵获取主数据库连接实例      参数1: 主数据库的名字(集群部署时在配置文件里指明)
            MASTER = MYSETINEL.master_for(**connection_dict["master_for"])
            # 通过哨兵获取从数据库连接实例    参数1: 从数据的名字(集群部署时在配置文件里指明)
            SLAVE = MYSETINEL.slave_for(**connection_dict["slave_for"])
            self.MYSETINEL = MYSETINEL
            self.MASTER = MASTER
            self.SLAVE = SLAVE
        except Exception as e:
            msg = str(e)
            if "password" in connection_dict:
                connection_dict["password"] = "*****"
            self.log(connection_dict)
            self.log(msg)
            return self.fail("登陆失败")
        return self.success({})

    def prepare(self):
        params_result = self.get_params_result()
        data_json_result = self.get_data_json(params_result)
        if not self.is_success(data_json_result):
            return data_json_result
        data_json_templ = self.get_data(data_json_result)
        data_json_result = self.get_ldap_param(data_json_templ, params_result)
        if not self.is_success(data_json_result):
            return data_json_result
        data_json = self.get_data(data_json_result)
        self.set_redis_template(data_json)

        conn_result = self.get_connection_from_template()
        if not self.is_success(conn_result):
            return conn_result
        return self.success("成功")

    def execute(self):

        redis_template = self.get_redis_template()
        data = {}
        if self.can_log():
            self.log(redis_template)
        try:

            target = getattr(self, redis_template["target"])
            params = get_safe_data("params", redis_template)
            method = getattr(target, redis_template["method"])
            # 单个执行
            if params:
                data = method(*params)
            params_list = get_safe_data("params_list", redis_template)
            # 执行批量
            if params_list:
                data = []
                for item in params_list:
                    method = getattr(target, item["method"])
                    data_item = method(*item["params"])
                    data.append(data_item)
        except Exception as e:
            return self.fail(str(e))

        return self.success(data)

    def execute_finish(self):

        try:
            self.MASTER.close()
            self.SLAVE.close()
        except Exception as e:
            self.log("redis 连接关闭异常：" + str(e))

    def result(self, params=None):
        prepare_result = self.prepare()
        if not self.is_success(prepare_result):
            return prepare_result
        execute_result = self.execute()
        if not self.is_success(execute_result):
            return execute_result
        data = self.get_data(execute_result)
        self.execute_finish()
        return self.success(data=data, msg="操作成功")
