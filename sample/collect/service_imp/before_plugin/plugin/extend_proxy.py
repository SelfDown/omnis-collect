# -*- coding: utf-8 -*-
"""
@Time: 2021/8/11 14:53
@Author: zzhang zzhang@cenboomh.com
@File: extend_param.py
@desc:
"""
from collect.service_imp.before_plugin.before_plugin import BeforePlugin
from collect.utils.collect_utils import get_safe_data


class ExtendProxy(BeforePlugin):
    ep_const = {
        "extend_proxy_name": "extend_proxy",
        "proxy_name": "proxy"
    }

    def get_extend_proxy_name(self):
        return self.ep_const["extend_proxy_name"]

    def get_proxy_name(self):
        return self.ep_const["proxy_name"]

    def extend_param_fields_name(self):
        return self.ep_const["extend_param_fields_name"]

    def handler(self, params, template):
        # self.log("进去添加参数插件")

        extend_proxy_service = get_safe_data(self.get_extend_proxy_name(), template)
        from collect.collect_service import CollectService
        collect_service = CollectService(op_user=self.op_user)
        result = collect_service.make_service(extend_proxy_service)
        if not self.is_success(result):
            return result
        proxy_service = self.get_data(result)
        proxy = get_safe_data(self.get_proxy_name(), proxy_service.template)
        import copy
        template[self.get_proxy_name()] = copy.deepcopy(proxy)
        return self.success(params)
