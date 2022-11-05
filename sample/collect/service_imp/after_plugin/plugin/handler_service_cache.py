from collect.service_imp.after_plugin.after_plugin import AfterPlugin
from collect.utils.collect_utils import get_safe_data


class HandlerServiceCache(AfterPlugin):
    HTConst = {
        "result_tag_name": "result_tag"
    }

    def get_result_tag_name(self):
        return self.HTConst["result_tag_name"]

    def handler(self, result, template):
        from collect.service_imp.common.service_cache_handler import ServiceCacheHandler
        params_result = self.get_params_result(template)
        h = ServiceCacheHandler(params_result, template)
        cache_config = get_safe_data(h.get_cache_name(), template)
        if not self.is_enable(params_result, cache_config):
            return self.success(result)
        h.set_cache(result)
        return self.success(result)
