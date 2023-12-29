# -*- coding: utf-8 -*-
"""
@Time: 2021/7/15 15:24
@Author: zzhang zzhang@cenboomh.com
@File: uuid.py
@desc:
"""
from collect.service_imp.common.filters.template_filters.base_filter import BaseFilter


class Base64EncodeFilter(BaseFilter):

    @staticmethod
    def filter(value):
        from base64 import b64encode
        return b64encode(value)
