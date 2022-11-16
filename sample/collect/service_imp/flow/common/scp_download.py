# -*- coding: utf-8 -*-
"""
@Time: 2021/8/17 10:15
@Author: zzhang zzhang@cenboomh.com
@File: ssh_copy.py
@desc:
"""
from collect.service_imp.flow.collect_ssh import CollectSSHService
from collect.utils.collect_utils import get_safe_data


class SCPDownload(CollectSSHService):
    def remote_file_exists(self, ssh, dest_path, template):
        result = self.execute_base_shell_with_log("ls " + dest_path, ssh, template=template)
        result_data = self.get_data(result)
        if self.has_error(result_data):
            return False
        else:
            return True

    def handler(self, params, config, template):
        from_path = get_safe_data(self.get_from_path_name(), config)
        if not from_path:
            return self.fail("配置中沒有找到来源文件位置")
        to_path = get_safe_data(self.get_to_path_name(), config)
        if not to_path:
            return self.fail("配置中沒有找到目标文件位置")
        from collect.service_imp.common.filters.template_tool import TemplateTool
        tool = TemplateTool(op_user=self.op_user)
        # if self.is_template_text(from_path):
        #     from_path = tool.render(from_path, params)
        from_path = self.get_render_data(from_path, params, tool=tool)

        # if self.is_template_text(to_path):
        #     to_path = tool.render(to_path, params)
        to_path = self.get_render_data(to_path, params, tool=tool)

        import os
        scp_result = self.get_scp_client(template)
        if not self.is_success(scp_result):
            return scp_result
        scp = self.get_data(scp_result)
        # dest_path = None
        # 如果目标文件“.”有后缀，表示是文件

        dest_path = os.path.dirname(to_path)
        dest_file = os.path.basename(to_path)

        if not os.path.exists(dest_path):
            os.makedirs(dest_path)
        try:
            if not dest_path.endswith("/"):
                dest_path += "/"
            dest = dest_path + dest_file
            scp.get(from_path, dest)
            size = os.path.getsize(dest)
        except Exception as e:
            msg = str(e)
            p = {"path": dest}
            msg = self.get_error_msg(msg, template, p)
            return self.fail(msg)
        d = {"path": dest, "size": size}
        return self.success(d)
