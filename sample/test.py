# -*- coding: utf-8 -*-
from jinja2 import Environment

import collect.service_imp.before_plugin.plugin.handler_req_param
import collect.service_imp.before_plugin.plugin.handler_params
# templ = "{% if is_windows== 'True' %}get_host{% else %}agentd_soft_install{% endif %}"
# # templ = "get_host"
# print templ
# print "-----------------------------------------------------------"
#
#
# def get_template_nodes(templ):
#     from jinja2 import Environment
#     env = Environment()
#     parsed_content = env.parse(templ)
#     content = parsed_content.body
#     result = []
#
#     def get_node(node):
#         node_list = []
#         if hasattr(node, "nodes"):
#             nodes = getattr(node, "nodes")
#             for node in nodes:
#                 data = getattr(node, "data")
#                 node_list.append(data)
#         for l in "body", "elif_", "else_":
#             node_list += get_nodes(node, l)
#         return node_list
#
#     def get_nodes(parent_node, name):
#         node_list = []
#         if not hasattr(parent_node, name):
#             return node_list
#         body = getattr(parent_node, name)
#         for child in body:
#             node_list += get_node(child)
#         return node_list
#
#     for item in content:
#         result += get_node(item)
#     return result
#
#
# print get_template_nodes(templ)
import collect.service_imp.before_plugin.plugin.handler_params
import collect.service_imp.result_handlers.handlers.result2excel
import collect.service_imp.request_rules.check
import collect.service_imp.before_plugin.plugin.handler_params
import collect.service_imp.request_handlers.handlers.service2field
import collect.service_imp.key_word_rules.require
# collect.service_imp.before_plugin.plugin.handler_params

import collect.service_imp.flow.common.gen_template
import collect.service_imp.request_rules.template
import collect.service_imp.common.filters.template_filters.json_str
import collect.service_imp.flow.common.scp_copy
import collect.service_imp.flow.collect_ssh

import collect.service_imp.ldap.ldap_service
import collect.service_imp.model.bulk_create
import collect.service_imp.sql.sql_update
import collect.service_imp.request_handlers.handlers.update_data
import collect.service_imp.common.filters.template_filters.date_time

import collect.service_imp.request_handlers.handlers.mul_arr
import collect.service_imp.request_handlers.handlers.ignore_data
import collect.service_imp.common.filters.template_filters.date_time
import collect.service_imp.common.filters.template_filters.current_day
import collect.service_imp.sql.sql_service
import collect.service_imp.after_plugin.plugin.handler_result
import collect.service_imp.common.filters.template_filters.des
import collect.service_imp.common.filters.template_filters.date_time
import collect.service_imp.session.session_service
from jira import JIRA
import collect.service_imp.model.model_delete
import collect.service_imp.request_handlers.handlers.service2field
import  collect.service_imp.request_handlers.handlers.excelData
import collect.service_imp.request_handlers.handlers.update_data
import collect.service.template_service
import collect.service_imp.flow.common.gen_template
import collect.service_imp.request_register.register.session
import collect.service_imp.request_register.register.session
import collect.service_imp.http.http_service

import collect.service_imp.common.filters.template_filters.ldap_password
import collect.service_imp.request_handlers.handlers.new_field
import collect.service_imp.test.test_service
import collect.service_imp.result_handlers.handlers.add_param
import collect.service_imp.model.bulk_create
import collect.service_imp.flow.collect_ssh
import collect.service_imp.request_register.register.header
# import subprocess
# proc = subprocess.Popen("ls",shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
# proc.wait()
# print proc.stdout.read()
# print proc.stderr.read()
# # stdout=io.TextIOWrapper(proc.stdout,encoding="utf-8")
# # stderr=io.TextIOWrapper(proc.stderr,encoding="utf-8")
# # import os
# # data = os.popen("cd F:/etc/ppp")
# # print data.read()
# import collect.service_imp.flow.common.server_archive

env = Environment()

t = env.from_string("{{1==1}}")
print t.render(**{})
