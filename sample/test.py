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
import collect.service_imp.request_handlers.handlers.excelData
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


import collect.service_imp.before_plugin.plugin.extend_proxy

# 192.168.10.133: | 操作失败 —— JAVA_HOME:  /usr/local/jdk1.8.0_301\nAPP_HOME:   /data/wghis/apps/cse-server\n开始启动进程 cse-server-bootstrap.jar\n进程启动成功，进程号 21175 —— cse-server-bootstrap.jar 的进程 20661 已关闭"

# err_msg: "{{server_ip}}:{{war_artifactid}} | {{bcs}}操作失败 —— {{startStatus}} —— {{stopStatus}}"
# t = env.from_string("{% if  deal_type=='stop' and  endProcess %} False {% elif deal_type!='stop'  and  (endProcess==startProcess  or not endProcess )  %} False {% else %} True {% endif %}")
# print t.render(**{"deal_type":"restart","endProcess":"","startProcess":"1111"})
# import collect.service_imp.ldap.ldap_service
params = {
    "service": "online_sql.create_sql",
    "data_base_type": "oracle",
    "op_type": "insert",
    "cols": [
        {
            "comment": "",
            "dbColType": "VARCHAR",
            "colIndex": 1,
            "id": "user_id",
            "name": "user_id",
            "field": "user_id",
            "width": 66.9140625,
            "sortable": True
        },
        {
            "comment": "",
            "dbColType": "VARCHAR",
            "colIndex": 2,
            "id": "nick",
            "name": "nick",
            "field": "nick",
            "width": 60,
            "sortable": True
        },
        {
            "comment": "",
            "dbColType": "VARCHAR",
            "colIndex": 3,
            "id": "user_name",
            "name": "user_name",
            "field": "user_name",
            "width": 94.4921875,
            "sortable": True
        },
        {
            "comment": "",
            "dbColType": "VARCHAR",
            "colIndex": 4,
            "id": "password",
            "name": "password",
            "field": "password",
            "width": 84.6875,
            "sortable": True
        },
        {
            "comment": "",
            "dbColType": "VARCHAR",
            "colIndex": 5,
            "id": "user_status",
            "name": "user_status",
            "field": "user_status",
            "width": 99.8203125,
            "sortable": True
        },
        {
            "comment": "",
            "dbColType": "VARCHAR",
            "colIndex": 6,
            "id": "entry_date",
            "name": "entry_date",
            "field": "entry_date",
            "width": 120,
            "sortable": True
        },
        {
            "comment": "",
            "dbColType": "VARCHAR",
            "colIndex": 7,
            "id": "email",
            "name": "email",
            "field": "email",
            "width": 60,
            "sortable": True
        },
        {
            "comment": "",
            "dbColType": "VARCHAR",
            "colIndex": 8,
            "id": "phone",
            "name": "phone",
            "field": "phone",
            "width": 60,
            "sortable": True
        },
        {
            "comment": "",
            "dbColType": "VARCHAR",
            "colIndex": 9,
            "id": "leave_date",
            "name": "leave_date",
            "field": "leave_date",
            "width": 120,
            "sortable": True
        },
        {
            "comment": "",
            "dbColType": "VARCHAR",
            "colIndex": 10,
            "id": "is_delete",
            "name": "is_delete",
            "field": "is_delete",
            "width": 78.484375,
            "sortable": True
        },
        {
            "comment": "",
            "dbColType": "VARCHAR",
            "colIndex": 11,
            "id": "create_time",
            "name": "create_time",
            "field": "create_time",
            "width": 120,
            "sortable": True
        },
        {
            "comment": "",
            "dbColType": "VARCHAR",
            "colIndex": 12,
            "id": "create_user",
            "name": "create_user",
            "field": "create_user",
            "width": 99.84375,
            "sortable": True
        },
        {
            "comment": "",
            "dbColType": "VARCHAR",
            "colIndex": 13,
            "id": "modify_user",
            "name": "modify_user",
            "field": "modify_user",
            "width": 105.140625,
            "sortable": True
        },
        {
            "comment": "",
            "dbColType": "VARCHAR",
            "colIndex": 14,
            "id": "modify_time",
            "name": "modify_time",
            "field": "modify_time",
            "width": 120,
            "sortable": True
        },
        {
            "comment": "",
            "dbColType": "VARCHAR",
            "colIndex": 15,
            "id": "work_code",
            "name": "work_code",
            "field": "work_code",
            "width": 93.5859375,
            "sortable": True
        },
        {
            "comment": "",
            "dbColType": "VARCHAR",
            "colIndex": 16,
            "id": "create_ldap",
            "name": "create_ldap",
            "field": "create_ldap",
            "width": 98.9375,
            "sortable": True
        },
        {
            "comment": "",
            "dbColType": "VARCHAR",
            "colIndex": 17,
            "id": "ladp_user_login_id",
            "name": "ladp_user_login_id",
            "field": "ladp_user_login_id",
            "width": 155.8125,
            "sortable": True
        },
        {
            "comment": "",
            "dbColType": "VARCHAR",
            "colIndex": 18,
            "id": "leave_reason",
            "name": "leave_reason",
            "field": "leave_reason",
            "width": 111.40625,
            "sortable": True
        },
        {
            "comment": "",
            "dbColType": "VARCHAR",
            "colIndex": 19,
            "id": "wechat_id",
            "name": "wechat_id",
            "field": "wechat_id",
            "width": 87.359375,
            "sortable": True
        },
        {
            "comment": "",
            "dbColType": "VARCHAR",
            "colIndex": 20,
            "id": "attendance_id",
            "name": "attendance_id",
            "field": "attendance_id",
            "width": 117.5859375,
            "sortable": True
        }
    ],
    "rowDatas": [
        {
            "wechat_id": "[NULL]",
            "user_status": "regular",
            "modify_user": "49ce12c3-b343-43ba-8478-335508726966",
            "user_id": "0997c859-46cd-46db-9679-f532176204e2",
            "attendance_id": "[NULL]",
            "phone": "13142130770",
            "is_delete": "0",
            "create_user": "739ade44-7e83-48a2-8c60-9a7c1e9f3d0a",
            "create_ldap": "1",
            "ladp_user_login_id": "ouyanghang",
            "work_code": "00112343",
            "nick": "欧阳航",
            "create_time": "2021-10-25 08:46:47",
            "entry_date": "2021-10-22",
            "leave_date": "",
            "leave_reason": "",
            "password": "a73609b15935a5c1ad32ae6ce684e518",
            "user_name": "ouyanghang",
            "email": "ouyanghang@weigaogroup.com",
            "modify_time": "2022-04-06 16:46:56",
            "index": 3,
            "id": 2
        }
    ],
    "primary_key": "user_id",
    "tablename": "username",
    "schdema": "eoms_formal"
}
# 19s 和0.096s
import time
env = Environment(cache_size=0,)
start = time.time()
sql_templ = "{{nick}}_{{uuid()}}"


def uuid():
    import uuid
    return str(uuid.uuid4())
t = env.from_string(sql_templ,globals={"uuid":uuid})
for i in range(1000000):
    params = {
        "nick": "张治"+str(i)
	}
    t.render(**params)

end = time.time()
print end - start
