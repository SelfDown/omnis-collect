# -*- coding: utf-8 -*-
"""
@Time: 2021/8/8 8:47
@Author: zzhang zzhang@cenboomh.com
@File: prop_arr.py
@desc:
"""
from collect.service_imp.common.filters.template_tool import TemplateTool
from collect.service_imp.request_handlers.request_handler import RequestHandler
from collect.utils.collect_utils import get_safe_data


class FilterArr(RequestHandler):
    faConst = {
        "ifTemplateName": "ifTemplate",
        "item_name": "item"
    }

    def get_item_save_name(self):
        return "itemSaveName"

    def get_item_if_template_name(self):
        return "itemIfTemplate"

    def get_item_value_template(self):
        return "itemIfTemplate"

    def getIfTemplateName(self):
        return self.faConst["ifTemplateName"]

    def getValueTemplateName(self):
        return "itemValueTemplate"

    def get_item_name(self):
        return self.faConst["item_name"]
    def get_fields_name(self):
        return "fields"
    def handler(self, params, config, template):

        foreach_name = get_safe_data(self.get_foreach_name(), config)

        if not foreach_name:
            return self.fail("过滤数组有找到 {params} 节点".format(params=self.get_foreach_name()))
        ifTemplate = get_safe_data(self.getIfTemplateName(), config)
        if not ifTemplate:
            return self.fail("过滤数组处理器 {params} 节点".format(params=self.getIfTemplateName(), ))
        save_field = get_safe_data(self.get_save_field_name(), config)

        foreach = get_safe_data(foreach_name, params)
        if not isinstance(foreach, list):
            return self.success(params)
        result_list = []
        tool = TemplateTool(op_user=self.op_user)
        item_name = get_safe_data(self.get_item_name(), config, "item")
        # 获取子字段名称
        field_name = get_safe_data(self.get_field_name(), config)
        # 获取保存字段名称
        itemSaveName = get_safe_data(self.get_item_save_name(), config)
        # 获取二级判断模板
        itemIfTemplate = get_safe_data(self.get_item_if_template_name(), config)
        # 获取二级取值模板
        itemValueTemplate = get_safe_data(self.getValueTemplateName(), config)

        saveConfigFields = get_safe_data(self.get_fields_name(),config)
        for item in foreach:
            item_result = []
            if itemSaveName:
                item[itemSaveName] = item_result

            val = self.get_render_data(ifTemplate, dict(params.items()+{item_name: item}.items()), tool)
            if val != self.get_true_value():
                continue
            result_list.append(item)
            field = get_safe_data(field_name,item,[])
            if len(field)<=0:
                continue
            if isinstance(field,list):
                for subItem in field:
                    itemIfVal = self.get_render_data(itemIfTemplate,dict(params.items()+subItem.items()),tool)
                    if itemIfVal!= self.get_true_value():
                        continue
                    if not saveConfigFields:
                        item_result.append(subItem)
                        continue
                    item_params=dict(subItem.items()+params.items())
                    item_val={}
                    for item_field in saveConfigFields:
                        item_fiel_name = get_safe_data(self.get_field_name(),item_field)
                        item_template = get_safe_data(self.get_template_name(),item_field)
                        item_value = self.render_data(item_template,item_params)
                        item_val[item_fiel_name]=item_value
                    item_result.append(item_val)
        params[save_field] = result_list

        return self.success(params)
