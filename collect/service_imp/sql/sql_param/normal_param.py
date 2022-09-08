# -*- coding: utf-8 -*-
from collect.service_imp.sql.sql_param.base_param import BaseParam


class NormalParam(BaseParam):
    split = "________________COLLECT_SQL_NORMAL_PARAM_SPLIT________________"
    """
    普通参数，将变量重新命名
    """

    def _ori_key(self):
        return "_"+self.param_key + self.split

    def get_param_key_list(self):
        """
         处理数组对象，额外参数,将变量重新命名
        """
        arr_key = self._ori_key()
        return [{self.get_attr_name(): arr_key, self.get_attr_value_name(): self.param_value}]
    def get_param_key_value(self, to_param_key):
        """
            获取字段名的参数值, 比如
            to_param_key
            为true ，直接返回字段名称，如果为false ，直接返回
            sql占位符号 ?。如果是数组则是，多个? 拼接的字符串
        """
        if to_param_key:
            return "{{" + self._ori_key() + "}}"
        else:
            param_key_value = '%s'
            return param_key_value
