# -*- coding: utf-8 -*-
"""
@Time: 2021/9/8 9:23
@Author: zzhang zzhang@cenboomh.com
@File: node_data.py
@desc:
"""
from collect.service_imp.flow.config_service import ConfigService
from collect.utils.collect_utils import get_safe_data


class InitNode(ConfigService):
    in_const = {

        "node_name": "node",
        "height_name": "height",
        "width_name": "width",
        "start_x_name": "start_x",
        "start_y_name": "start_y",
        "distance_name": "distance",
        "condition_name": "condition"

    }

    def get_condition_name(self):
        return self.in_const["condition_name"]

    def get_node_name(self):
        return self.in_const["node_name"]

    def get_distance_name(self):
        return self.in_const["distance_name"]

    def get_height_name(self):
        return self.in_const["height_name"]

    def get_width_name(self):
        return self.in_const["width_name"]

    def get_start_x_name(self):
        return self.in_const["start_x_name"]

    def get_start_y_name(self):
        return self.in_const["start_y_name"]

    def get_template_nodes(self, templ):
        if not templ:
            return []
        from jinja2 import Environment
        env = Environment()
        parsed_content = env.parse(templ)
        content = parsed_content.body
        result = []

        def get_node(node):
            node_list = []
            if hasattr(node, "nodes"):
                nodes = getattr(node, "nodes")
                for node in nodes:
                    data = getattr(node, "data")
                    node_list.append(data)
            for l in "body", "elif_", "else_":
                node_list += get_nodes(node, l)
            return node_list

        def get_nodes(parent_node, name):
            node_list = []
            if not hasattr(parent_node, name):
                return node_list
            body = getattr(parent_node, name)
            for child in body:
                node_list += get_node(child)
            return node_list

        for item in content:
            result += get_node(item)
        return result

    def handler(self, params, config, template):
        node_name = get_safe_data(self.get_node_name(), config)
        if not node_name:
            return self.fail("配置中沒有找到" + self.get_node_name())
        height_name = get_safe_data(self.get_height_name(), config)
        if not height_name:
            return self.fail("配置中沒有找到" + self.get_height_name())
        width_name = get_safe_data(self.get_width_name(), config)
        if not width_name:
            return self.fail("配置中沒有找到" + self.get_width_name())
        start_x_name = get_safe_data(self.get_start_x_name(), config)
        if not start_x_name:
            return self.fail("配置中沒有找到" + self.get_start_x_name())

        start_y_name = get_safe_data(self.get_start_y_name(), config)
        if not start_y_name:
            return self.fail("配置中沒有找到" + self.get_start_y_name())
        distance_name = get_safe_data(self.get_distance_name(), config)
        if not distance_name:
            return self.fail("配置中沒有找到" + self.get_distance_name())

        tool = self.get_render_tool()
        params_result = self.get_params_result(template)
        nodes = self.get_render_data(node_name, params_result, tool)
        if not nodes:
            return self.fail("参数中没有找到" + node_name)
        width = self.get_render_data(width_name, params_result, tool)
        if not width:
            return self.fail("参数中没有找到" + width_name)
        height = self.get_render_data(height_name, params_result, tool)
        if not height:
            return self.fail("参数中没有找到" + height_name)
        start_x = self.get_render_data(start_x_name, params_result, tool)
        if not width:
            return self.fail("参数中没有找到" + start_x)
        start_y = self.get_render_data(start_y_name, params_result, tool)
        if not start_y:
            return self.fail("参数中没有找到" + start_y_name)
        distance = self.get_render_data(distance_name, params_result, tool)
        if not start_y:
            return self.fail("参数中没有找到" + distance_name)

        node_dict = {}
        for node in nodes:
            key = get_safe_data(self.get_key_name(), node)
            node_dict[key] = node
        parse_node_dict = {}
        for key in node_dict:
            node = node_dict[key]
            next = get_safe_data(self.get_next_name(), node)
            next_node_keys = self.get_template_nodes(next)
            if len(next_node_keys) <= 1:
                parse_node_dict[key] = node
                continue

            import copy
            condition = copy.deepcopy(node)
            condition_name = self.get_condition_name()
            new_key = key + "_" + condition_name
            condition[self.get_type_name()] = condition_name
            condition[self.get_key_name()] = new_key
            condition["desc"] = condition[self.get_next_name()]
            condition[self.get_name_name()] = "智能条件"
            condition[self.get_next_name()] = next_node_keys
            node[self.get_next_name()] = new_key
            parse_node_dict[key] = node
            parse_node_dict[new_key] = condition

        target_node_dict = {}

        # current_node = self.get_start_node(parse_node_dict)
        # start_key = get_safe_data(self.get_key_name(), current_node)
        def get_target_node(node):
            desc = get_safe_data("desc", node)
            if not desc:
                desc = get_safe_data(self.get_name_name(), node)
            target = {
                'id': get_safe_data(self.get_key_name(), node),
                'width': width,
                'height': height,
                'coordinate': [node["x"], node["y"]],
                'meta': {
                    'prop': get_safe_data(self.get_type_name(), node),
                    'name': get_safe_data(self.get_name_name(), node),
                    'desc': desc
                }
            }
            return target

        def handler_target_node(key, parent, node_y=None):
            current = get_safe_data(key, parse_node_dict)
            if "x" in current:
                return
            if not parent:
                x = start_x
                y = start_y
            else:

                parent_node = get_safe_data(parent, parse_node_dict)
                x = get_safe_data("x", parent_node, 0)
                y = get_safe_data("y", parent_node, 0)
                x += distance
            current["x"] = x

            if node_y:
                y = node_y
            elif current[self.get_type_name()] == "end":
                y = start_y
            current["y"] = y
            next = get_safe_data(self.get_next_name(), current)
            if isinstance(next, str):
                handler_target_node(next, get_safe_data(self.get_key_name(), current))
            elif isinstance(next, list):
                node_start_y = y - distance * len(next) / 2
                for index, child in enumerate(next):
                    node_y = node_start_y + distance * index * 2
                    handler_target_node(child, get_safe_data(self.get_key_name(), current), node_y)

        handler_target_node(self.get_start_name(), None)
        target_list = []
        for key in parse_node_dict:
            target = get_target_node(parse_node_dict[key])
            target_list.append(target)
        # current_node = self.get_start_node(node_dict)
        # # last=current_node
        # end_node = self.get_end_node(parse_node_dict)
        # for i in range(100):
        #     if current_node == end_node:
        #         handler_target_node(self.get_end_name())
        #         continue
        #     next = get_safe_data(self.get_next_name(), current_node)
        #     if isinstance(next, str):
        #
        #         handler_target_node(next)
        #     elif isinstance(next,list):
        #         for item in next:
        #             handler_target_node(item)
        # node_list = []
        # for index, node in enumerate(nodes):
        #     # self.get_start_node()
        #     node_new = {
        #         'id': get_safe_data(self.get_key_name(), node),
        #         'width': width,
        #         'height': height,
        #         'coordinate': [start_x + index * distance, start_y],
        #         'meta': {
        #             'prop': get_safe_data(self.get_type_name(), node),
        #             'name': get_safe_data(self.get_name_name(), node),
        #             'desc': get_safe_data(self.get_name_name(), node)
        #         }
        #     }
        #     node_list.append(node_new)

        return self.success(target_list)
