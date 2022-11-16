# -*- coding: utf-8 -*-
"""
@Time: 2021/8/16 13:50
@Author: zzhang zzhang@cenboomh.com
@File: collect_ssh.py
@desc:
"""

# from collect.collect_service import CollectService
from collect.service_imp.flow.collect_flow import ServiceCollectFlowService
from collect.utils.collect_utils import get_safe_data

ssh_error_info_path = './conf/ssh_error_info.yml'
#  这里判断文件是否存在
import os

if not os.path.exists(ssh_error_info_path):
    raise Exception("根目下没有找到" + ssh_error_info_path + "文件", )
with open(ssh_error_info_path, 'r') as f:
    import yaml

    error_info = yaml.load(f)


class CollectSSHService(ServiceCollectFlowService):
    ssh_app_config = None
    ssh_const = {
        "user_name": "user",
        "password_name": "password",
        "server_ip_name": "server_ip",
        "port_name": "port",
        "timeout_name": "timeout",
        "ssh_client_name": "ssh_client",
        "scp_client_name": "scp_client",
        "error_msg_name": "error_msg",
        "shell_name": "shell",
        "shell_list_name": "shell_list",
        "services_name": "services",
        "shell_flow_name": "shell_flow",
        "ssh_name": "ssh",
        "from_path_name": "from",
        "to_path_name": "to",
        "ssh_connect_name": "ssh_connect",

    }
    data_json_dict = {}

    @staticmethod
    def get_json_content(path):
        return get_safe_data(path, CollectSSHService.data_json_dict)

    @staticmethod
    def set_json_content(path, data_json_content):
        CollectSSHService.data_json_dict[path] = data_json_content

    def get_ssh_connect_name(self):
        return self.ssh_const["ssh_connect_name"]

    def get_from_path_name(self):
        return self.ssh_const["from_path_name"]

    def get_to_path_name(self):
        return self.ssh_const["to_path_name"]

    def get_ssh_name(self):
        return self.ssh_const["ssh_name"]

    def get_shell_flow_name(self):
        return self.ssh_const["shell_flow_name"]

    def has_error(self, msg):
        return self.get_error_info(msg)

    def get_error_info(self, msg):
        global error_info
        for item in error_info["info"]:
            if item[self.get_key_name()] in msg:
                return item[self.get_template_name()]

    def get_error_msg_name(self):
        return self.ssh_const["error_msg_name"]

    def get_error_msg(self, msg, template=None, p={}):
        template = self.get_template_data(template)
        templ = self.get_error_info(msg)
        if not templ:
            return msg
        from collect.service_imp.common.filters.template_tool import TemplateTool
        tool = TemplateTool(op_user=self.op_user)
        params = self.get_params_result(template)
        params[self.get_error_msg_name()] = msg
        if p:
            params = dict(params.items() + p.items())
        return tool.render(templ, params)

    def get_shell_name(self):
        return self.ssh_const["shell_name"]

    def get_shell_list_name(self):
        return self.ssh_const["shell_list_name"]

    def get_user_name(self):
        return self.ssh_const["user_name"]

    def get_ssh_client_name(self):
        return self.ssh_const["ssh_client_name"]

    def get_scp_client_name(self):
        return self.ssh_const["scp_client_name"]

    def get_user(self):
        return get_safe_data(self.get_user_name(), self.get_params_result())

    def get_password_name(self):
        return self.ssh_const["password_name"]

    def get_password(self):
        return get_safe_data(self.get_password_name(), self.get_params_result())

    def get_server_ip_name(self):
        return self.ssh_const["server_ip_name"]

    def get_server_ip(self):
        return get_safe_data(self.get_server_ip_name(), self.get_params_result())

    def get_timeout_name(self):
        return self.ssh_const["timeout_name"]

    def get_timeout(self):
        timeout = get_safe_data(self.get_timeout_name(), self.get_params_result(), 15)
        return int(timeout)

    def get_port_name(self):
        return self.ssh_const["port_name"]

    def get_port(self):
        port = get_safe_data(self.get_port_name(), self.get_params_result(), 22)
        return int(port)

    def __init__(self, op_user):
        ServiceCollectFlowService.__init__(self, op_user=op_user)
        if not CollectSSHService.ssh_app_config:
            CollectSSHService.ssh_app_config = self.get_third_application(self.get_ssh_name())

    def get_app_config(self):
        return CollectSSHService.ssh_app_config

    def get_ssh_data(self, template=None):
        return self.get_data(self.get_ssh_client(template))

    def get_scp_client(self, template=None):

        params_result = self.get_params_result(template)
        scp = get_safe_data(self.get_scp_client_name(), params_result)
        if not scp:
            ssh_result = self.get_ssh_client(template)
            if not self.is_success(ssh_result):
                return ssh_result

            ssh = self.get_data(ssh_result)
            try:
                scp = ssh.open_sftp()
            except Exception as e:
                msg = str(e)
                msg = self.get_error_msg(msg)
                return self.fail(msg)
            params_result[self.get_scp_client_name()] = scp
        return self.success(scp)

    def get_ssh_client(self, template=None):
        params_result = self.get_params_result(template)
        ssh = get_safe_data(self.get_ssh_client_name(), params_result)
        if not ssh:
            import paramiko
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                ssh.connect(self.get_server_ip(),
                            self.get_port(),
                            self.get_user(),
                            self.get_password(),
                            timeout=self.get_timeout(), banner_timeout=10,
                            look_for_keys=False)
            except Exception as e:
                msg = str(e)
                msg = self.get_error_msg(msg)
                return self.fail(msg)
            params_result[self.get_ssh_client_name()] = ssh
        return self.success(ssh)

    def prepare(self):
        ssh_connect_name = self.get_ssh_connect_name()
        if ssh_connect_name in self.template:
            ssh_connect = get_safe_data(self.get_ssh_client_name(), self.template)
        else:
            ssh_connect = True

        if not self.get_server_ip():
            ssh_connect = False
        if ssh_connect:
            ssh_client = self.get_ssh_client()
            if not self.is_success(ssh_client):
                return ssh_client
        return self.success("检查完毕")

    def get_shell(self):
        if get_safe_data(self.get_data_json_name(), self.template):
            data_json_result = self.get_data_json(self.get_params_result())
            if not self.is_success(data_json_result):
                return data_json_result
            data_json = self.get_data(data_json_result)
            import json
            data_json = json.loads(data_json)
            return data_json
        return get_safe_data(self.get_shell_name(), self.template)

    def get_services_name(self):
        return self.ssh_const["services_name"]

    def get_services(self):
        shell = self.get_shell()
        if not shell:
            return
        return get_safe_data(self.get_services_name(), shell)

    def execute(self, handler_node):
        # 设置流程节点
        self.set_flow(self.get_shell())
        self.set_flow_name(self.get_shell_flow_name())
        flow_result = self.flow(handler_node)
        return flow_result

    def execute_finish(self):
        params_result = self.get_params_result()
        ssh = get_safe_data(self.get_ssh_client_name(), params_result)

        if ssh:
            ssh.close()
            del params_result[self.get_ssh_client_name()]
        scp = get_safe_data(self.get_scp_client_name(), params_result)
        if scp:
            scp.close()
            del params_result[self.get_scp_client_name()]

        return self.success("执行结束")

    def get_node_shell(self, node):
        shell_script = self.get_node_shell_list_script(node)
        if shell_script:
            return shell_script
        shell = get_safe_data(self.get_shell_name(), node)
        return shell

    def get_node_shell_list_script(self, node):
        shell_list = get_safe_data(self.get_shell_list_name(), node)
        if not shell_list:
            return
        s = [get_safe_data(self.get_shell_name(), item) for item in shell_list]
        return ";".join(s)

    def get_node_shell_list_save_fields(self, node):
        shell_list = get_safe_data(self.get_shell_list_name(), node)
        if not shell_list:
            return
        s = [get_safe_data(self.get_save_field_name(), item) for item in shell_list]
        return s

    def log_shell(self, shell, password=None, template=None):
        if password:
            shell_show = shell.replace(password, "******")
        else:
            shell_show = shell
        self.log(shell_show, template=template)

    def execute_base_shell_with_log(self, shell, ssh=None, password=None, template=None):
        template = self.get_template_data(template)
        if self.can_log(template):
            self.log_shell(shell, password, template=template)
        if not ssh:
            ssh = self.get_ssh_data()

        env = 'source .bash_profile;source /etc/profile;export LANG=en_US.UTF-8;'
        try:
            stdin, stdout, stderr = ssh.exec_command('%s%s' % (env, shell),timeout=15*60)
            stdin.write("n")
            result = ''.join(str(stdout.read()) + str(stderr.read()))
            result = str(result).strip()
        except Exception as e:
            result = "exec error。执行命令："+shell+"，执行超时"
        return self.success(result)

    def handler_current_node(self, current):
        shell = self.get_node_shell(current)
        result = None
        # 如果shell 命令存在，先处理shell
        ignore_error = get_safe_data(self.get_ignore_error_name(), current, False)
        if shell:
            if self.is_template_text(shell):
                from collect.service_imp.common.filters.template_tool import TemplateTool
                tool = TemplateTool(op_user=self.op_user)
                shell = tool.render(shell, self.get_params_result())
            shell_result = self.execute_base_shell_with_log(shell)
            result = self.get_data(shell_result)
            if not ignore_error and self.has_error(result):
                return self.fail(self.get_error_msg(result))
            # 处理批量shell 的保存字段
            save_fields = self.get_node_shell_list_save_fields(current)
            if save_fields and result:
                result_list = result.split("\n")
                params_result = self.get_params_result()
                # 依次处理save_field和结果的关系，结果中有换行就会有问题
                for result_item, save_field in zip(result_list, save_fields):
                    params_result[save_field] = result_item

        # 处理第三方模块，比如文件上传，服务器拷贝文件
        config = self.get_app_config()
        result = self.handler_app(current, config, result)
        if not self.is_success(result):
            return result
        result = self.get_data(result)

        if not ignore_error and self.has_error(result):
            return self.fail(self.get_error_msg(result))
        return self.success(result)

    def result(self, params):
        params_result = self.get_params_result()
        prepare_result = self.prepare()
        if not self.is_success(prepare_result):
            return prepare_result
        execute_result = self.execute(handler_node=self.handler_current_node)
        err_msg = None
        err = False
        if not self.is_success(execute_result):
            err_msg = self.get_msg(execute_result)
            err = True

        finish_result = self.execute_finish()
        if not self.is_success(finish_result):
            return finish_result
        if err:
            return self.fail(err_msg)
        return self.success({})
