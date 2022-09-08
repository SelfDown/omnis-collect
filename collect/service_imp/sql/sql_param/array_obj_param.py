# -*- coding: utf-8 -*-
from collect.service_imp.sql.sql_param.base_param import BaseParam
import copy


class ArrayObjParam(BaseParam):
    """
    数组对象参数，核心思想就是将数组变量打平，变成线性变量
    """
    split = "________________COLLECT_SQL_OBJ_ARR_PARAM_SPLIT________________"

    def is_array(self):
        return True

    def _ori_arr_key(self, index, field):
        return self.param_key + self.split + str(index) + self.split + field

    def get_arr_key(self, index, field):
        """
        获取数组对象的key
        """
        return "{{" + self._ori_arr_key(index, field) + "}}"

    def get_param_key_list(self):
        """获取数组对象变量列表"""
        data_list = self.param_value
        key_list = []
        for index, item in enumerate(data_list):
            for field in self.child_param_keys:
                arr_key = self._ori_arr_key(index, field)
                if field in item:
                    value = item[field]
                else:
                    value = None
                key_list.append(self.get_attr_param(arr_key, value))

        return key_list

    def get_real_value(self):
        """
        获取实际数据值
        """
        data_list = self.param_value
        value_list = []
        for index, item in enumerate(data_list):
            for field in self.child_param_keys:
                if field in item:
                    value_list.append(item[field])
                else:
                    value_list.append(None)
        return value_list

    def get_param_key_value(self, to_param_key):
        """
            获取字段名的参数值, 比如
            to_param_key
            为true ，直接返回字段名称，如果为false ，直接返回
            sql占位符号 ?。如果是数组则是，多个? 拼接的字符串
        """

        data_list = copy.deepcopy(self.param_value)
        for index, item in enumerate(data_list):
            for field in self.child_param_keys:
                arr_key = self.get_arr_key(index, field)
                item[field] = arr_key

        return data_list
