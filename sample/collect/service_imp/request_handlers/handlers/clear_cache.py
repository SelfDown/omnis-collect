# -*- coding: utf-8 -*-
"""
@Time: 2021/7/26 15:31
@Author: zzhang zzhang@cenboomh.com
@File: updateData.py
@desc:
"""
from collect.service_imp.common.filters.template_tool import TemplateTool
from collect.service_imp.request_handlers.request_handler import RequestHandler
from collect.utils.collect_utils import get_safe_data


class ClearCache(RequestHandler):
    def get_clear_room_name(self):
        return "clear_room"
    def handler(self, params, config, template):
        from collect.service_imp.common.service_cache_handler import ServiceCacheHandler
        h = ServiceCacheHandler(params, template)
        h.set_cache_config(config)
        room_list = get_safe_data(self.get_clear_room_name(),config)
        for room in room_list:
            h.set_room(get_safe_data(self.get_key_name(),room))
            h.clear_cache()
        return self.success(params)
