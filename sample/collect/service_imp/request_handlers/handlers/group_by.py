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


class GroupBy(RequestHandler):

    def get_group_detail_name(self):
        return "group_detail"
    def get_group_detail_name(self):
        return "group_detail"

    def get_fields_name(self):
        return "fields"
    def get_group_fields_name(self):
        return "group_fields"

    def get_key(self, fields, item):
        value_list = []

        for field in fields:
            field_name = field[self.get_field_name()]
            value_list.append(str(item[field_name]))

        return "[#]".join(value_list)

    def get_key_obj(self, fields, item, detail_name,group_fields):
        item_result = {}
        for field in fields:
            field_name = field[self.get_field_name()]
            item_result[field_name] = item[field_name]
            item_result[detail_name] = [item]
            for subField in group_fields:
                sub_field_name = subField[self.get_field_name()]
                item_result[sub_field_name] = item[sub_field_name]
        return item_result

    def handler(self, params, config, template):
        foreach_name = get_safe_data(self.get_foreach_name(), config)
        if not foreach_name:
            return self.fail("没有找到foreach ，在group_by中")
        foreach = self.render_data(foreach_name, params)
        detail_name = get_safe_data(self.get_group_detail_name(), config, self.get_group_detail_name())
        if not foreach:
            return self.success(params)
        fields = get_safe_data(self.get_fields_name(), config)
        if not fields:
            return self.fail("没有找到fields ，在group_by中")
        group_dict = {}
        group_fields=get_safe_data(self.get_group_fields_name(),config)
        for item in foreach:
            key = self.get_key(fields, item)
            if key not in group_dict:
                data =self.get_key_obj(fields, item, detail_name,group_fields)
                group_dict[key]= data
            else:
                group_dict[key][detail_name].append(item)
        data_list = group_dict.values()
        save_field = get_safe_data(self.get_save_field_name(), config)
        if save_field:
            params[save_field] = data_list
        return self.success(params)
