# -*- coding: utf-8 -*-
"""
@Time: 2021/8/26 14:58
@Author: zzhang zzhang@cenboomh.com
@File: arr2arrobj.py
@desc:
"""
from collect.service_imp.request_handlers.request_handler import RequestHandler
from collect.utils.collect_utils import get_safe_data


class Arr2ArrObj(RequestHandler):
    """
    数组列表，转数组对象
    """
    aao_const = {
        "obj_name": "obj",
        "item_name": "item",
    }

    def get_obj_name(self):
        return self.aao_const["obj_name"]

    def get_item_name(self):
        return self.aao_const["item_name"]
    def get_sub_item_name(self):
        return "sub_item"

    def handler(self, params, config, template):
        foreach_name = get_safe_data(self.get_foreach_name(), config)
        if not foreach_name:
            return self.fail(self.get_foreach_name() + "字段配置不存在")

        foreach = get_safe_data(foreach_name, params)
        if not foreach:
            return self.fail(self.get_foreach_name() + "不能为空")

        save_field_name = get_safe_data(self.get_save_field_name(), config)
        if not save_field_name:
            return self.fail(self.get_save_field_name() + "字段配置不存在")
        sub_field_name = get_safe_data(self.get_sub_item_name(), config)


        obj = get_safe_data(self.get_obj_name(), config)
        if not obj:
            return self.fail(self.get_obj_name() + "字段配置不存在")
        from collect.service_imp.common.filters.template_tool import TemplateTool
        tool = TemplateTool(op_user=self.op_user)
        l = []
        def get_obj(obj,p):
            data = {}
            for key in obj:
                templ = obj[key]
                v = self.get_render_data(templ, p, tool)
                data[key] = v
            return data
        for item in foreach:
            p = dict(self.get_params_result(template).items()+{self.get_item_name(): item}.items())
            if not sub_field_name:# 如果是个一级数组
                l.append(get_obj(obj,p))
            else:# 如果是个二级数组
                for sub_item in foreach[item]:
                    p[sub_field_name]=sub_item
                    l.append(get_obj(obj, p))
        params[save_field_name] = l
        return self.success(params)
