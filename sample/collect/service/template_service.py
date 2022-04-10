# -*- coding: utf-8 -*-
"""
@Time: 2021/6/28 17:01
@Author: zzhang zzhang@cenboomh.com
@File: template_service.py
@desc:
"""
from collect.collect_service import CollectService
from collect.utils.collect_utils import get_safe_data, Singleton


@Singleton
class TemplateService(CollectService):
    TSConst = {
        "http_name": "http",
        "set_template_method_name": "set_template_method",
        "get_template_method_name": "get_template_method"
    }

    def __init__(self, op_user=None):
        CollectService.__init__(self, op_user)
        self.op_user = op_user
        self.session = None
        self.request = None

    def get_set_template_method_name(self):
        return self.TSConst["set_template_method_name"]

    def get_get_template_method_name(self):
        return self.TSConst["get_template_method_name"]

    def get_http_name(self):
        return self.TSConst["http_name"]

    def http_check(self, template):
        success = get_safe_data(self.get_http_name(), template, False)
        if success:
            return self.success([])
        else:
            return self.fail("不支持http 访问")

    def set_session(self, session):
        self.session = session

    def get_request(self):
        return self.request

    def set_request(self, request):
        self.request = request

    # def get_session(self,template=None):
    #     return self.session

    def result(self, data, is_http=False):
        service = get_safe_data("service", data)
        if not service:
            return self.fail("服务不能为空")
        # collect_service = CollectService(op_user=self.op_user)
        # collect_service.set_session(self.get_session())
        collect_service = self

        # self.set_session(self.get_session())
        result = collect_service.make_service(service)
        # 初始化对象返回结果
        if not collect_service.is_success(result):
            return result

        service_obj = collect_service.get_data(result)
        service_obj.setIsHttp(is_http)
        # 如果是http 直接请求
        # 数据对象的设置，设置session，header
        request_register = self.get_request_register()
        if is_http:  # 如果是http 就生成
            http_result = self.http_check(service_obj.get_template())
            # http 检查返回结果
            if not collect_service.is_success(http_result):
                return http_result

            for register in request_register:
                path = register[self.get_path_name()]
                class_name = register[self.get_class_name()]
                try:
                    import importlib
                    register_factory = importlib.import_module(path)
                    register_obj = getattr(register_factory, class_name)(op_user=self.op_user)
                    # 插件设置请求对象，
                    register_obj.set_request(self.get_request())
                    get_data_method = getattr(register_obj, register[self.get_method_name()])
                    register_data = get_data_method()
                    if not self.is_success(register_data):
                        return register_data
                    register_data = self.get_data(register_data)
                    set_data_method = getattr(service_obj, register[self.get_set_template_method_name()])
                    set_data_method(register_data)
                except Exception as e:
                    return self.fail(class_name + "找不到，请检查配置" + str(e))
        else:  # 如果非http 就从上级获取
            self.handler_self_register_data(service_obj)
            # for register in request_register:
            #     path = register[self.get_path_name()]
            #     class_name = register[self.get_class_name()]
            #     try:
            #         get_data_method = getattr(self, register[self.get_get_template_method_name()])
            #         register_data = get_data_method()
            #         set_data_method = getattr(service_obj, register[self.get_set_template_method_name()])
            #         set_data_method(register_data)
            #     except Exception as e:
            #         return self.fail(class_name + "找不到，请检查配置" + str(e))

        # 查询数据
        params = data
        # # # 所有接口必须登录检查
        # login_check = service_obj.login_check()
        # if not collect_service.is_success(login_check):
        #     return login_check
        # 执行前处理
        before_result = service_obj.before_result(params)
        if not service_obj.is_success(before_result) or self.is_finish(before_result):
            return before_result
        # 执行结果
        return_result = service_obj.result(params)
        if not service_obj.is_success(return_result):
            return return_result
        data = service_obj.get_data(return_result)
        count = service_obj.get_count(return_result)
        msg = service_obj.get_msg(return_result)
        # 获取结果后处理器
        after_result = service_obj.after_result(data)
        if not self.is_success(after_result):
            return after_result
        # 设置处理之后的结果
        data = self.get_data(after_result)
        # 获取处理之后的消息
        after_msg = self.get_msg(after_result)
        if after_msg:
            msg = after_msg
        other = None
        other_result = self.get_other(after_result)
        if other_result:
            other = other_result
        return self.success(data, msg=msg, count=count, other=other)
