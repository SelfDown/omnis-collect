# -*- coding: utf-8 -*-
from django.core.cache import caches

from collect.utils.collect_utils import get_safe_data


class ServiceCacheHandler:
    def __init__(self, params, template):
        self.cache_config = get_safe_data(self.get_cache_name(), template)
        self._cache = caches["default"]
        self.params = params
        pass

    def get_cache_name(self):
        return "cache"

    def get_fields(self):
        return self.cache_config["fields"]

    def get_second(self):
        return get_safe_data("second", self.cache_config, 30)

    def get_field_name(self):
        return "field"

    def get_cache_key(self):
        fields = self.get_fields()
        value_list = []
        for field in fields:
            field_name = get_safe_data(self.get_field_name(), field)
            value_list.append(get_safe_data(field_name, self.params,""))
        return "_service_cache"+"#".join(value_list)

    def set_cache(self, data):
        self._cache.set(self.get_cache_key(), data, self.get_second())

    def get_cache(self):
        return self._cache.get(self.get_cache_key())
