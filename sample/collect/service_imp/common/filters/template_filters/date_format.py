# -*- coding: utf-8 -*-
"""
@Time: 2021/7/15 15:54
@Author: zzhang zzhang@cenboomh.com
@File: date_time.py
@desc:
"""
from collect.service_imp.common.filters.template_filters.base_filter import BaseFilter


class DateFormat(BaseFilter):

    # @staticmethod
    def filter(self, value, fmt, to_fmt):
        from collect.utils.collect_utils import transferDateTime
        return transferDateTime(value, fmt, to_fmt)
