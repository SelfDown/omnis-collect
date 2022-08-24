# -*- coding: utf-8 -*-
from collect.utils.collect_utils import get_safe_data, get_key

from collect.service_imp.before_plugin.before_plugin import BeforePlugin


class ServiceProxy(BeforePlugin):
    SPConst = {
        "proxy_name":"proxy",
        "proxy_service_name":"proxy_service_name"
    }
    def get_proxy_name(self):
        return self.SPConst["proxy_name"]
    def get_proxy_service_name(self):
        return self.SPConst["proxy_service_name"]

    def handler(self, params, template):
        isFinish = False
        proxy = get_safe_data(self.get_proxy_name(),template)
        # 如果不可用则，跳过
        if not self.is_enable(params,proxy):
            return self.success(params)
        current_service = self.get_current_service(template)
        proxy_service_name= get_safe_data(self.get_proxy_service_name(),proxy)
        if not proxy_service_name:
            return self.fail("代理服务，没有配置"+self.get_proxy_service_name())
        params[proxy_service_name] = current_service
        service_data = self.get_node_service(node=proxy, params=params, template=template, append_param=True)
        if not self.is_success(service_data):
            return service_data
        service = self.get_data(service_data)
        service_result = self.get_service_result(service, template)
        if not self.is_success(service_result):
            self.log(self.get_msg(service_result), template=template)
            self.log(proxy, template=template)
            return service_result
        isFinish = True
        data = self.get_data(service_result)
        return self.success(data,finish=isFinish)
