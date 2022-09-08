# -*- coding: utf-8 -*-
from collect.service_imp.sql.sql_param.base_param import BaseParam
import copy


class ArrayParam(BaseParam):
    """
    数组对象参数，核心思想就是将数组变量打平，变成线性变量
    """
    split = "________________COLLECT_SQL_ARR_PARAM_SPLIT________________"

    def is_array(self):
        return True

    def _ori_arr_key(self, index):
        return self.param_key + self.split + str(index) + self.split

    def get_arr_key(self, index):
        """
        获取数组对象的key
        """
        return "{{" + self._ori_arr_key(index) + "}}"

    def get_param_key_list(self):
        """获取数组对象变量列表"""
        data_list = copy.deepcopy(self.param_value)
        key_list = []
        for index, item in enumerate(data_list):
            arr_key = self._ori_arr_key(index)
            key_list.append(self.get_attr_param(arr_key, item))
        return key_list

    def get_real_value(self):
        """
        获取实际数据值
        """
        return self.param_value

    def get_param_key_value(self, to_param_key):
        """
            获取字段名的参数值, 比如
            to_param_key
            为true ，直接返回字段名称，如果为false ，直接返回
            sql占位符号 ?。如果是数组则是，多个? 拼接的字符串
        """

        data_list = copy.deepcopy(self.param_value)
        l = []
        if to_param_key:
            for index, item in enumerate(data_list):
                arr_key = self.get_arr_key(index, )
                l.append(arr_key)
            return ",".join(l)
