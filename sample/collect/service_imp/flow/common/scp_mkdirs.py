# -*- coding: utf-8 -*-
"""
@Time: 2021/8/17 10:15
@Author: zzhang zzhang@cenboomh.com
@File: ssh_copy.py
@desc:
"""
from collect.service_imp.common.filters.template_tool import TemplateTool
from collect.service_imp.flow.collect_ssh import CollectSSHService
from collect.utils.collect_utils import get_safe_data


class SCPMkdirs(CollectSSHService):
    def remote_file_exists(self, scp, dest_path, template):
        try:
            scp.lstat(dest_path)
            return True
        except Exception as e:
            return False
        # result = self.execute_base_shell_with_log("ls " + dest_path, ssh, template=template)
        # result_data = self.get_data(result)
        # if self.has_error(result_data):
        #     return False
        # else:
        #     return True

    def mkdirs(self, scp, dest_path, template):
        try:
            import os
            dest = dest_path.replace("\\","/")
            dest_arr = dest.split("/")
            dest_arr = [item for item in dest_arr if item]
            for index,dir in enumerate(dest_arr):
                dir_all="/"+"/".join(dest_arr[0:index+1])
                if not self.remote_file_exists(scp,dir_all,template):
                    scp.mkdir(dir_all)

            return True, "创建成功"
        except Exception as e:
            return False, "文件夹创建失败【"+dest_path+"】详情："+str(e)
        # result = self.execute_base_shell_with_log("mkdir -p  " + dest_path, ssh, template=template)
        # result_data = self.get_data(result)
        # if self.has_error(result_data):
        #     return False, result_data
        # else:
        #     return True, ""

    def handler(self, params, config, template):
        pathTpl = get_safe_data("remote_path", config)
        loalPathTpl = get_safe_data("local_path", config)
        tool = TemplateTool(op_user=self.op_user)
        if pathTpl:

            path = self.get_render_data(pathTpl, params, tool=tool)
            scp_result = self.get_scp_client(template)
            if not self.is_success(scp_result):
                return scp_result
            scp = self.get_data(scp_result)
            if not self.remote_file_exists(scp, path, template):
                status, result_data = self.mkdirs(scp, path, template)
                if not status:
                    return self.fail(result_data)
        if loalPathTpl:
            local_path = self.get_render_data(loalPathTpl, params, tool=tool)
            import os
            if not os.path.exists(local_path):
                os.makedirs(local_path)
        return self.success("创建完成")
