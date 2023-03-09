# -*- coding: utf-8 -*-
"""
@Time: 2021/7/15 15:24
@Author: zzhang zzhang@cenboomh.com
@File: uuid.py
@desc:
"""
from collect.service_imp.common.filters.template_filters.base_filter import BaseFilter
from collect.utils.collect_utils import get_uuid


class RegSumFilter(BaseFilter):

    @staticmethod
    def filter(value, reg):
        import re
        result = re.findall(reg, value)
        if result:
            sum_data = 0
            for item in result:
                try:
                    sum_data += int(item)
                except Exception as e:
                    pass
            return sum_data
        else:
            return "0"
