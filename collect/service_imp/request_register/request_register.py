# -*- coding: utf-8 -*-
from collect.collect_service import CollectService
from collect.utils.collect_utils import get_safe_data


class RequestRegister(CollectService):
    """
    请求对象注册
    """

    def __init__(self, op_user):
        CollectService.__init__(self, op_user)
        self.request = None

    def set_request(self, request):
        self.request = request

    def get_request(self):
        return self.request
