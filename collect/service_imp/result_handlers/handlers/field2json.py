# -*- coding: utf-8 -*-
"""
@Time: 2021/8/24 9:02
@Author: zzhang zzhang@cenboomh.com
@File: field2json.py
@desc:
"""
from collect.service_imp.result_handlers.result_handler import ResultHandler
from collect.utils.collect_utils import get_safe_data


class Field2JSONService(ResultHandler):
    def handler(self, result, config, template):
        # 如果是空对象，直接返回
        if not result:
            return self.success(result)
        field = get_safe_data(self.get_field_name(), config)
        if isinstance(result, list):
            for item in result:
                if field in item and item[field]:
                    import json
                    try:
                        item[field] = json.loads(item[field])
                    except Exception as e:
                        continue
        elif isinstance(result, str) or isinstance(result, unicode):
            import json
            result = json.loads(result)
        return self.success(result)
