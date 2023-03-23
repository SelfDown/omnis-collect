# -*- coding: utf-8 -*-
from collect.utils.collect_utils import get_safe_data, get_key

from collect.service_imp.before_plugin.before_plugin import BeforePlugin


class ServiceCache(BeforePlugin):
    SCConst = {

    }

    def handler(self, params, template):
        from collect.service_imp.common.service_cache_handler import ServiceCacheHandler
        h = ServiceCacheHandler(params, template)
        cache_config = get_safe_data(h.get_cache_name(), template)
        if not self.is_enable(params, cache_config):
            return self.success(params)
        # 这里逻辑要重新思考下，有点丑陋
        # 想做的是定时任务，还差60s 判断是销毁，定时任务是判断销毁，重新请求。
        # 但是普通请求不会，防止缓存间隙
        if get_safe_data("session_user_id",params) == "sys":
            has = h.has_key()
            if not has:
                return self.success(params)
        result = h.get_cache()
        if result is not None:
            service_result = self.success(result)
            service_result["finish"] = True
            return service_result

        return self.success(params)
