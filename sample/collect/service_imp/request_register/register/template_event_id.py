# -*- coding: utf-8 -*-
from collect.service_imp.request_register.request_register import RequestRegister


class TemplateEventID(RequestRegister):
    """
    日志事件ID
    """

    def get_register_data(self):
        """
        获取注册数据
        """

        from collect.utils.collect_utils import get_uuid
        return self.success(get_uuid())
