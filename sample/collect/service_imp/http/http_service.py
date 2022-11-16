# -*- coding: utf-8 -*-
"""
@Time: 2021/7/14 16:32
@Author: zzhang zzhang@cenboomh.com
@File: ModelUpdate.py
@desc:
"""
from collect.collect_service import CollectService
from collect.utils.collect_utils import get_safe_data, DateEncoder


class HttpService(CollectService):
    HConst = {
        "data_json_name": "data_json",
        "success_name": "success",
        "append_param_name": "append_param",
        "data_name": "data",
        "params_name": "params",
        "method_name": "method",
        "get_name": "get",
        "post_name": "post",
    }

    data_json_dict = {}

    @staticmethod
    def get_json_content(path):
        return get_safe_data(path, HttpService.data_json_dict)

    @staticmethod
    def set_json_content(path, data_json_content):
        HttpService.data_json_dict[path] = data_json_content

    def __init__(self, op_user):
        CollectService.__init__(self, op_user)
        self.api = HttpApi(op_user)
        pass

    def get_method_get_name(self):
        return self.HConst["get_name"]

    def get_method_post_name(self):
        return self.HConst["post_name"]

    def get_method_name(self):
        return self.HConst["method_name"]

    def get_success_name(self):
        return self.HConst["success_name"]

    def get_data_name(self):
        return self.HConst["data_name"]

    def get_params_name(self):
        return self.HConst["params_name"]

    def get_append_param_name(self):
        return self.HConst["append_param_name"]

    # def get_data_json_name(self):
    #     return self.HConst["data_json_name"]
    #
    # def get_data_json_config_path(self):
    #     data_json = get_safe_data(self.get_data_json_name(), self.template)
    #
    #     config_dir = self.get_config_dir()
    #     config_file = config_dir + "/" + data_json
    #     return config_file
    #
    # def get_data_json(self, params):
    #     config_file_path = self.get_data_json_config_path()
    #     json_content = self.get_json_content(config_file_path)
    #     if json_content:
    #         return self.success(json_content)
    #     data_json = get_safe_data(self.get_data_json_name(), self.template)
    #     data_json_result = self.get_config_file(data_json, params)
    #     if self.is_success(data_json_result):
    #         data_json_content = self.get_data(data_json_result)
    #         self.set_json_content(config_file_path, data_json_content)
    #     return data_json_result

    def get_http_param(self, data_json_templ, params_result, append_param=False):
        from collect.service_imp.common.filters.template_tool import TemplateTool
        tool = TemplateTool(op_user=self.op_user)
        data_json = tool.render(data_json_templ, params_result)

        try:
            import json
            data_json = json.loads(data_json)
            # 拼接剩下的参数
            if append_param:
                # 查询是否配置data
                data = get_safe_data(self.get_data_name(), data_json)
                # 如果配置配置data 取params
                if not data:
                    data = get_safe_data(self.get_data_name(), data_json)
                if not data:
                    method = get_safe_data(self.get_method_name(), data_json, self.get_method_get_name())
                    data = {}
                    if method.lower() == self.get_method_get_name():
                        data_json[self.get_params_name()] = data
                    else:
                        data_json[self.get_data_name()] = data
                for attr_key in params_result:
                    if attr_key not in data:
                        data[attr_key] = params_result[attr_key]

            if self.can_log():
                self.log(data_json)
            return self.success(data_json)
        except Exception as e:
            self.log(data_json, "error")
            return self.fail(str(e) + " JSON格式有误，请检查配置")

    def result(self, params=None):
        params_result = self.get_params_result()

        success_temp = get_safe_data(self.get_success_name(), self.template)
        # if not success_temp:
        #     return self.fail("HTTP请求模块没有配置" + self.get_success_name())
        data_json_result = self.get_data_json(params_result)
        if not self.is_success(data_json_result):
            return data_json_result
        data_json_templ = self.get_data(data_json_result)
        append_param = get_safe_data(self.get_append_param_name(), self.template, False)
        data_json_result = self.get_http_param(data_json_templ, params_result, append_param)
        if not self.is_success(data_json_result):
            return data_json_result
        data_json = self.get_data(data_json_result)

        result = self.api.send(data_json, template=self.template)
        if not self.is_success(result):
            return result
        result_data = self.get_data(result)
        if success_temp and isinstance(result_data, dict):
            from collect.service_imp.common.filters.template_tool import TemplateTool
            tool = TemplateTool(op_user=self.op_user)
            val = self.get_render_data(success_temp, result_data, tool)
            if self.is_false(val):
                err_msg = get_safe_data(self.get_err_msg_name(), self.template)
                if not err_msg:
                    return self.fail("HTTP 模块没有配置" + self.get_err_msg_name())
                message = self.get_render_data(err_msg, result_data, tool)
                fail = self.fail(message)
                fail["other"] = self.get_other(result_data)
                return fail
        params_result["http_send"] = data_json
        msg = self.get_msg(result_data)
        count = self.get_count(result_data)
        if not msg:
            msg = "发送成功"
        other = self.get_other(result_data)
        return self.success(data=result_data, msg=msg, count=count, other=other)


class HttpApi(CollectService):

    def __init__(self, op_user):
        """
         调用监控模块
        """
        CollectService.__init__(self, op_user)

    def handler_param(self, data):
        """
         处理参数
        """
        if "auth" in data:
            # 处理登录
            from requests.auth import HTTPBasicAuth
            auth = HTTPBasicAuth(**data["auth"])
            data["auth"] = auth
        if "data" in data and "headers" in data:
            target = data["data"]
            headers = data["headers"]
            for key in data["headers"]:
                content = headers[key].lower()
                if key.lower() == 'content-type' and content == 'application/json':
                    try:
                        import json
                        data["data"] = json.dumps(target, cls=DateEncoder)
                    except Exception as e:
                        self.log("JSON格式失败", level="error")
                        self.log(target)

    def send(self, data, template=None):
        import requests
        import json
        self.handler_param(data)
        try:
            r = requests.request(**data)
        except Exception as e:
            self.log("请求发送失败", level="error", template=template)
            self.log(data, level="error", template=template)
            self.log(str(e), level="error", template=template)
            # self.log(template, level="error", template=template)
            return self.fail(msg=str(e))
        if r.status_code >= 400:
            result_data = r.text[0:10000]
            self.log(r.text, template=template)
            self.log(r.status_code, template=template)
            r.close()
            del (r)
            return self.fail(result_data)
        try:
            # print len(r.text)
            # if len(r.text)!=0:
            result_data = r.json()
            if result_data == None:
                result_data=""
            # result_data = json.loads(r.text)
            # else:
            #     result_data = ""
            r.close()
            del (r)
        except Exception as e:
            self.log("数据返回错误：" + str(e) + "\n\n" + r.text, template=template)
            return self.fail(msg="数据返回格式错误")

        return self.success(result_data)
