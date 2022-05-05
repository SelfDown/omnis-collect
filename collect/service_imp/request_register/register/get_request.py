# -*- coding: utf-8 -*-
from collect.service_imp.request_register.request_register import RequestRegister


class GetRequest(RequestRegister):
    """
    request.Meta 注冊,包含请求头
    """

    def get_register_data(self):
        """
        获取注册数据
        """
        request = self.get_request()
        if not request:
            return self.fail(msg="请求requests对象不存在")
        return self.success(request)
