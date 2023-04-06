# -*- coding: utf-8 -*-
"""
@Time: 2021/8/28 18:40
@Author: zzhang zzhang@cenboomh.com
@File: get_array_obj.py
@desc:
"""
from collect.service_imp.request_handlers.request_handler import RequestHandler
from collect.utils.collect_utils import get_safe_data


class ObjInArray(RequestHandler):
    gao_const = {
        "from_array_name": "from_array",
        "to_obj_array_name": "to_obj_array"
    }

    def get_from_array_name(self):
        return self.gao_const["from_array_name"]

    def get_to_obj_array_name(self):
        return self.gao_const["to_obj_array_name"]

    def get_target_name(self):
        return "target"

    def get_fields_name(self):
        return "fields"

    def get_target_name(self):
        return "target"

    def handler(self, params, config, template):
        foreach_name = get_safe_data(self.get_foreach_name(), config)
        if not foreach_name:
            return self.fail("获取数组对象处理器没有找到 {params} 节点".format(params=self.get_foreach_name()))
        foreach = get_safe_data(foreach_name, params)
        if foreach is None:
            return self.fail("获取数组对象处理器,没有找到{field}".format(field=foreach_name))
        fields = get_safe_data(self.get_fields_name(), config)
        if not fields:
            return self.fail("获取数组对象处理器,没有找到{field}".format(field=self.get_fields_name()))
        target_name = get_safe_data(self.get_target_name(), config)
        if not target_name:
            return self.fail("获取数组对象处理器,没有找到{field}".format(field=self.get_target_name()))
        save_field = get_safe_data(self.get_save_field_name(), config)
        if not target_name:
            return self.fail("获取数组对象处理器,没有找到{field}".format(field=self.get_target_name()))
        target = get_safe_data(target_name, params)
        if not target:
            return self.fail("获取数组对象处理器,没有找到{field}".format(field=target_name))

        def get_key(data):
            lf = [data[field] for field in data if field in fields]
            return "#".join(lf)

        target_key = get_key(target)
        has = False
        for item in foreach:
            if get_key(item) == target_key:
                has = True
        params[save_field] = has
        return self.success(params)
