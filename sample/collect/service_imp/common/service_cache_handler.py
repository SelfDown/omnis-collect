# -*- coding: utf-8 -*-
from django.core.cache import caches

from collect.utils.collect_utils import get_safe_data


class ServiceCacheHandler:
    def __init__(self, params, template):
        self.cache_config = get_safe_data(self.get_cache_name(), template)
        self._cache = caches["default"]
        self.params = params
        pass

    def set_cache_config(self, config):
        self.cache_config = config

    def set_room(self, room):
        self.cache_config["room"] = room

    def get_cache_name(self):
        return "cache"

    def get_fields(self):
        return self.cache_config["fields"]

    def get_room(self):
        return get_safe_data("room", self.cache_config)

    def get_second(self):
        return get_safe_data("second", self.cache_config, 0)

    def get_field_name(self):
        return "field"

    def get_ttl_gt_name(self):
        return "ttl_gt"

    def get_cache_key(self):
        fields = self.get_fields()
        value_list = []
        for field in fields:
            field_name = get_safe_data(self.get_field_name(), field)
            value_list.append(str(get_safe_data(field_name, self.params, "")))
        service_key = "_service_cache" + "#".join(value_list)
        room = self.get_room()
        if not room:
            return service_key
        return "_room_" + room + ":[" + service_key + "]"

    def set_cache(self, data):
        timeout = self.get_second()
        if timeout <= 0:
            timeout = None
        self._cache.set(self.get_cache_key(), data, timeout)

    def get_cache(self):
        return self._cache.get(self.get_cache_key())

    def has_key(self):
        key = self.get_cache_key()
        ttl_gt = get_safe_data(self.get_ttl_gt_name(), self.cache_config)
        if not ttl_gt:
            return self._cache.has_key(key)
        ttl = self._cache.ttl(key)
        if ttl is None:
            return False
        if ttl < 0 or ttl > ttl_gt:
            return True
        else:
            return False

    def clear_cache(self):
        if self._cache.has_key(self.get_cache_key()):
            self._cache.delete(self.get_cache_key())
