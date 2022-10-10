# -*- coding: utf-8 -*-
"""
@Time: 2021/7/14 16:32
@Author: zzhang zzhang@cenboomh.com
@File: ModelUpdate.py
@desc:
"""
from collect.service_imp.model.model_delete import ModelDeleteService
from collect.utils.collect_utils import get_safe_data


class ModelUpdateService(ModelDeleteService):
    MUConst = {
        "update_fields_name": "update_fields",
        "field_options_name": "field_options"
    }

    def __init__(self, op_user):
        ModelDeleteService.__init__(self, op_user)

        pass

    def get_update_fields_name(self):
        return self.MUConst["update_fields_name"]

    def get_field_options_name(self):
        return self.MUConst["field_options_name"]

    def result(self, params=None):
        result = self.handler_model_params(params)
        if self.finish or not self.is_success(result):
            return result
        # 获取模型对象
        model_obj_result = self.get_model_obj()
        if not self.is_success(model_obj_result):
            return model_obj_result
        model_obj = self.get_data(model_obj_result)
        filter_result = self.get_model_filter()
        if not self.is_success(filter_result):
            return filter_result
        c = self.get_count(filter_result)
        query_filter = self.get_data(filter_result)
        u_fields = get_safe_data(self.get_update_fields_name(), self.get_template())
        field_options = get_safe_data(self.get_field_options_name(), self.get_template())
        params_result = self.get_params_result()
        # 处理前台传参数，选择控制修改部分属性,不传则改所有属性，传就只改传了的属性。
        # 是基于update_fields 中的，不能超出update_fields 中的属性
        if field_options:
            req_fields = self.render_data(field_options, params_result, [])
            if req_fields:
                # 如果传请求字段，则取请求里面的字段，如果有* 则取所有
                if "*" not in req_fields:
                    u_fields = [item for item in u_fields if item in req_fields]
            if not req_fields or not u_fields:
                if self.can_log():
                    self.log("没有找到任何更新属性，直接返回")
                    self.log(req_fields)
                return self.success(data={}, msg="修改 【0】条记录成功", count=0)


        es_fields = get_safe_data(self.get_exclude_save_field_name(), self.get_template())
        update_fields = self.get_update_fields(model_obj, update_fields=u_fields,
                                               exclude_save_field=es_fields)
        if len(update_fields) == 0:
            return self.fail(msg="没有找到更新字段")

        if c == 0:
            if self.can_log():
                self.log(msg="警告！！！没有找到更新记录")
            return self.success(data={}, msg="修改 【0】条记录成功")
        update_obj = {}
        # params_result = self.get_params_result()
        if self.can_log():
            self.log("更新字段")
            self.log(update_fields)
        for key in update_fields:
            update_obj[key] = params_result[key]

        update_sum = query_filter.update(**update_obj)
        if self.can_log():
            self.log("影响行数：" + str(update_sum))
        if update_sum != c:
            return self.success(data={}, msg="总共修改【{c}】 条。修改 【{update_sum}】条记录成功".format(c=str(c),
                                                                                         update_sum=str(update_sum)))
        return self.success(data={}, msg="修改 【{c}】条记录成功".format(c=str(update_sum)), count=c)
