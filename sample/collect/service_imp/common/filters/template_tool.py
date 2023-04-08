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
from collect.utils.collect_utils import get_safe_data

_cache = {}


class TemplateTool(CollectService):
    def load_filter(self, env, templ, params, config_params, template):
        filter_config = self.get_filter_handler()
        for key in filter_config:

            if isinstance(templ, str) and key not in templ:
                continue
            rule = filter_config[key]
            path = rule[self.get_path_name()]
            class_name = rule[self.get_class_name()]
            import importlib
            filter_factory = importlib.import_module(path)
            rule_obj = getattr(filter_factory, class_name)(params=params,
                                                           config_params=config_params,
                                                           template=template,
                                                           current_key=key,
                                                           op_user=self.op_user)
            method = getattr(rule_obj, rule[self.get_method_name()])
            ft = get_safe_data("type", rule)
            if ft == "func":
                env.globals[key] = method
            else:
                env.filters[key] = method

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
            if templ not in _cache:
                env = Environment()
                self.load_filter(env, templ, params, config_params, template)
                t = env.from_string(templ)
                _cache[templ] = t
            else:
                t = _cache[templ]
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
