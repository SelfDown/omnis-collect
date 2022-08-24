# -*- coding: utf-8 -*-
class BaseParam:
    def __init__(self, param_key, param_value=None, child_param_keys=None):
        """初始化"""
        self.param_key = param_key
        self.param_value = param_value
        self.child_param_keys = child_param_keys

    def is_array(self):
        return False
    def get_attr_param(self,arr_key,item):
        return {self.get_attr_name(): arr_key, self.get_attr_value_name(): item}

    def get_attr_name(self):
        return "attr"

    def get_attr_value_name(self):
        return "value"

    def get_attr_name_value(self, p):
        return p[self.get_attr_name()]

    def get_attr_value_name_value(self, p):
        return p[self.get_attr_value_name()]

    def get_param_key_list(self):
        """
         处理数组对象，额外参数,将变量重新命名
        """
        return []

    def set_param_value(self, value):
        """设置原始值"""
        self.param_value = value

    def get_real_value(self):
        """
        获取实际数据值
        """
        return [self.param_value]

    def get_param_key(self):
        """获取key"""
        return self.param_key

    def get_param_key_value(self, to_param_key):
        """
            获取字段名的参数值, 比如
            to_param_key
            为true ，直接返回字段名称，如果为false ，直接返回
            sql占位符号 ?。如果是数组则是，多个? 拼接的字符串
        """
        if to_param_key:
            return "{{" + self.param_key + "}}"
        else:
            param_key_value = '%s'
            return param_key_value
