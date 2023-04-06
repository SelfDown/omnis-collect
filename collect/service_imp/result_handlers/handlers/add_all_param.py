# -*- coding: utf-8 -*-
"""
@Time: 2021/8/4 14:17
@Author: zzhang zzhang@cenboomh.com
@File: new_col.py
@desc:
"""
from collect.service_imp.result_handlers.result_handler import ResultHandler
from collect.utils.collect_utils import get_safe_data


class AddAllParam(ResultHandler):
    ap_const = {

    }

    def get_from_self_name(self):
        return "from_self"
    def get_prefix_name(self):
        return "prefix"
    def get_reg_name(self):
        return "reg"
    def handler(self, result, config, template):
        field = get_safe_data(self.get_field_name(), config)
        if not field:
            return self.fail("添加处理器没有找到 {params} 节点".format(params=self.get_field_name()))
        from_self = get_safe_data(self.get_from_self_name(), config, False)
        prefix = get_safe_data(self.get_prefix_name(), config)
        reg_value = get_safe_data(self.get_reg_name(), config)
        params = self.get_params_result(template)

        if not from_self:
            if field == '.':
                obj= params
            else:
                obj = get_safe_data(field, params)
            if not obj:
                return self.success(obj)
            if not isinstance(obj, dict):
                return self.fail("添加处理器没有找到 {params} 节点,非字典对象".format(params=self.get_field_name()))

        def handler_data(data):
            if from_self:  # 如果来源自己，则从自己取对象
                target = get_safe_data(field, data, {})
            else:  # 如果来源参数
                target = obj
            items = target.items()
            # 正则表达式过滤
            if reg_value:
                import re
                items = [item for item in items if item[0] and len(re.findall(reg_value, item[0]))>0]
            # 如果配置了前缀
            if prefix:
                items=[(prefix+item[0],item[1]) for item in items if item[0]]
            return dict(data.items() + items)

        if isinstance(result, list):
            lr = []
            for item in result:
                lr.append(handler_data(item))
        else:
            lr = handler_data(result)
        return self.success(lr)
