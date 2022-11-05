# -*- coding: utf-8 -*-
"""
@Time: 2021/8/11 14:53
@Author: zzhang zzhang@cenboomh.com
@File: extend_param.py
@desc:
"""
from collect.service_imp.before_plugin.before_plugin import BeforePlugin
from collect.utils.collect_utils import get_safe_data


class ExtendCache(BeforePlugin):
    ec_const = {
        "extend_cache_name": "extend_cache",
        "cache_name": "cache"
    }

    def get_extend_cache_name(self):
        return self.ec_const["extend_cache_name"]

    def get_cache_name(self):
        return self.ec_const["cache_name"]

    def handler(self, params, template):
        # self.log("进去添加参数插件")

        extend_cache_service = get_safe_data(self.get_extend_cache_name(), template)
        from collect.collect_service import CollectService
        collect_service = CollectService(op_user=self.op_user)
        result = collect_service.make_service(extend_cache_service)
        if not self.is_success(result):
            return result
        cache_service = self.get_data(result)
        cache = get_safe_data(self.get_cache_name(), cache_service.template)
        import copy
        template[self.get_cache_name()] = copy.deepcopy(cache)
        return self.success(params)
