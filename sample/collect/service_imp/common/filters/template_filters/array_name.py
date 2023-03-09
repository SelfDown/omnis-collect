# -*- coding: utf-8 -*-
"""
@Time: 2021/7/21 15:56
@Author: zzhang zzhang@cenboomh.com
@File: foreach.py
@desc:
"""
from collect.service_imp.common.filters.template_filters.base_filter import BaseFilter
from collect.service_imp.common.filters.template_tool import TemplateTool
from collect.utils.collect_utils import get_safe_data


class ArrayNameFilter(BaseFilter):

    def filter(self, value, *args, **kargs):
        """

        :param value:
        :return:
        """
        if not value:
            return ""
        name = get_safe_data(self.get_name_name(), kargs)
        join = get_safe_data(self.get_join_name(), kargs)
        msg_list = []
        for item in value:
            msg = get_safe_data(name, item)
            msg_list.append(msg)
        return join.join(msg_list)
