# -*- coding: utf-8 -*-
"""
@Time: 2021/9/2 14:54
@Author: zzhang zzhang@cenboomh.com
@File: dir_tree.py
@desc:
"""
from collect.service_imp.flow.collect_ssh import CollectSSHService
from collect.utils.collect_utils import get_safe_data, get_uuid


class Command(CollectSSHService):

    def handler(self, params, config, template):

        from collect.service_imp.common.filters.template_tool import TemplateTool
        tool = TemplateTool(op_user=self.op_user)
        command = self.get_render_data(config, params, tool)
        if self.can_log(template):
            self.log(command, template=template)
        import subprocess
        proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
        proc.wait()
        err = proc.stderr.read()
        normal = proc.stdout.read()
        result = err + normal
        # 解码
        try:
            tmp = result.decode("gbk").encode("utf8")
            result = tmp
        except Exception as e:
            pass
        # 如果失败了，则失败返回
        if self.has_error(result):
            self.get_error_msg(msg=result, template=template)
        return self.success(result)
