# -*- coding: utf-8 -*-
"""
@Time: 2021/6/28 17:01
@Author: zzhang zzhang@cenboomh.com
@File: template_service.py
@desc:
"""
from collect.collect_service import CollectService
from collect.utils.collect_utils import get_safe_data, Singleton


# @Singleton
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
    def get_schedule_services(self, always=False):
        router = self.get_items_router()
        service_list = []
        index = 0
        for project in router:
            for service in router[project]:
                serviceData = router[project][service]
                if "schedule" in serviceData:
                    schedule = get_safe_data("schedule", serviceData)
                    if not schedule:
                        continue
                    if always == True and "always" not in schedule:
                        continue
                    enable = get_safe_data("enable", schedule, "")
                    if enable:

                        enableVar = self.render_data(enable, {})
                        if enableVar != self.get_true_value():
                            continue

                    def schedule_func(data):
                        def f():
                            try:

                                result = self.result(data)
                                if not get_safe_data("success", result):
                                    self.log(data)
                                    self.log(result)
                                    del result

                            except Exception as e:
                                pass

                        return f

                    parameter = get_safe_data("parameter", schedule)
                    if not parameter:
                        continue
                    if enable is "" or enableVar == self.get_true_value():
                        index += 1
                        s = project + "." + service
                        self.log("添加定时服务:" + str(index))
                        self.log(s)
                        self.log(parameter)
                        parameter["func"] = schedule_func(data={
                            "service": s,
                        })
                        service_list.append(parameter)
        return service_list

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
        def handler_register(register):
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
                return self.success([])
            except Exception as e:
                return self.fail(class_name + "找不到，请检查配置" + str(e))

        request_register = self.get_request_register()
        if is_http:  # 如果是http 就生成
            http_result = self.http_check(service_obj.get_template())
            # http 检查返回结果
            if not collect_service.is_success(http_result):
                return http_result
            for register_item in request_register:
                register_result = handler_register(register_item)
                if not self.is_success(register_result):
                    return register_result
        else:  # 如果非http 就从上级获取
            self.handler_self_register_data(service_obj)
        # 主要处理手动调用TemplateService 服务，非http 不能生成event_id
        always_register = self.get_always_request_register()
        if always_register:  # 处理template 里面event_id,加上always 标签
            class_name = always_register[self.get_class_name()]
            try:
                # 先获取service_obj 里面的对象，是否有值
                get_data_method = getattr(service_obj, always_register[self.get_get_template_method_name()])
                register_data = get_data_method()
                if not register_data:  # 如果不存在值,则生成
                    handler_register(always_register)
            except Exception as e:
                return self.fail(class_name + "找不到，请检查配置" + str(e))

        # 查询数据
        params = data

        # # # 所有接口必须登录检查
        # login_check = service_obj.login_check()
        # if not collect_service.is_success(login_check):
        #     return login_check
        # 执行前处理
        def handler_err_other(service_obj, resultMap):
            if not self.get_other(resultMap):
                after_result = service_obj.after_result(None, True)
                resultMap["other"] = self.get_other(after_result)

        before_result = service_obj.before_result(params)
        # 如果结束执行，则是直接返回
        if self.is_finish(before_result):
            # 由于直接返回，没有运行参数，所以这里设下下参数，否则tag 取不到
            service_obj.set_params_result(params)
            handler_err_other(service_obj, before_result)
            return before_result
        # 如果执行失败，则处理下结果加上，tag
        if not service_obj.is_success(before_result):
            handler_err_other(service_obj, before_result)
            return before_result
        # 执行结果
        return_result = service_obj.result(params)
        if not service_obj.is_success(return_result):
            handler_err_other(service_obj, return_result)
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
        # 计算本地tag
        other_result = self.get_other(after_result)
        if other_result:
            other = other_result
        # 如果结果有tag ，优先结果里面的tag
        if self.get_other(return_result):
            other = self.get_other(return_result)
        return self.success(data, msg=msg, count=count, other=other)
