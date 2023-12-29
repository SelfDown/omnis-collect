# -*- coding: utf-8 -*-
"""
@Time: 2021/7/16 13:58
@Author: zzhang zzhang@cenboomh.com
@File: template_tool.py
@desc:
"""

from jinja2 import Environment

from collect.collect_service import CollectService

# 全局变量缓存模板信息
from collect.utils.collect_utils import get_safe_data, Singleton


@Singleton
class TemplateTool(CollectService):
    def __init__(self, op_user=None):
        CollectService.__init__(self, op_user)
        self._cache = {}
        self._node_code = {}

    def load_filter(self, env, templ):
        filter_config = self.get_filter_handler()
        for key in filter_config:

            if isinstance(templ, str) and key not in templ:
                continue
            rule = filter_config[key]

            path = rule[self.get_path_name()]
            class_name = rule[self.get_class_name()]
            import importlib
            filter_factory = importlib.import_module(path)
            rule_obj = getattr(filter_factory, class_name)()
            method = getattr(rule_obj, rule[self.get_method_name()])
            ft = get_safe_data("type", rule)
            if ft == "func":
                env.globals[key] = method
            else:
                env.filters[key] = method

    def parse_node(self, templ):
        if not self._node_code.has_key(templ):
            env = Environment()
            t = env.parse(templ)
            self._node_code[templ] = t
        else:
            t = self._node_code.get(templ)
        return t

    def gen_template(self, templ):
        if not self._cache.has_key(templ):
            env = Environment()
            self.load_filter(env, templ)
            t = env.from_string(templ)
            self._cache[templ] = t
        else:
            t = self._cache.get(templ)
        return t

    def render(self, templ, params, config_params=None, template=None):
        templ = str(templ)
        # if not isinstance(templ, str):
        #     return templ
        # if templ in _cache:
        #     t = _cache[templ]["temp"]
        #     # env = _cache[templ]["env"]
        # else:
        from django.http import QueryDict
        if isinstance(params, QueryDict):
            try:
                params = params.dict()
            except Exception as  e:
                pass

        try:
            t = self.gen_template(templ)
            if params and isinstance(params, dict) and 'self' in params:
                del params['self']
            if None in params:
                del params[None]
            result_content = t.render(**params)
        except Exception as e:
            self.log(templ + "运行报错：" + str(e) + " 请检查配置！！！", template=template)
            return ""

        data = result_content.strip()
        del result_content
        if data == "None":
            data = ""
        return data
