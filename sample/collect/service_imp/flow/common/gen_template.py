# -*- coding: utf-8 -*-
"""
@Time: 2021/8/17 10:15
@Author: zzhang zzhang@cenboomh.com
@File: ssh_copy.py
@desc:
"""
from collect.service_imp.flow.collect_ssh import CollectSSHService
from collect.utils.collect_utils import get_safe_data


class GenTemplate(CollectSSHService):
    # GTConst = {
    #     # "templ_name": "templ"
    #
    # }
    #
    # def get_templ_name(self):
    #     return self.GTConst["templ_name"]

    def handler(self, params, config, template):

        to_path = get_safe_data(self.get_to_path_name(), config)
        if not to_path:
            return self.fail("配置中沒有找到目标文件位置")
        from collect.service_imp.common.filters.template_tool import TemplateTool
        tool = TemplateTool(op_user=self.op_user)
        templ_name = get_safe_data(self.get_template_name(), config)
        import os
        if not templ_name:
            # 来源模板数据
            from_path = get_safe_data(self.get_from_path_name(), config)
            if not from_path:
                return self.fail("配置中沒有找到来源文件位置")
            from_path = self.get_render_data(from_path, params, tool=tool)

            if not os.path.exists(from_path):
                return self.fail(from_path + "文件不存在")
            if os.path.isdir(from_path):
                return self.fail(from_path + "是个文件夹，不支持")
            with open(from_path) as f:
                templ = f.read()
        else:
            templ = self.get_render_data(templ_name, params, tool, nullToTemplateField=False)

        if not templ:
            if self.can_log(template):
                self.log("警告!!!文件内容为空，请检查是否需要输出空文件", template)

        to_path = self.get_render_data(to_path, params, tool=tool)
        to_dir = os.path.dirname(to_path)
        if not os.path.exists(to_dir):
            os.makedirs(to_dir)
        content = tool.render(templ, params)
        import re
        content_unix = re.sub(r'\r\n', r'\n', content)
        if self.can_log(template):
            self.log("生成文件:" + to_path)
            self.log(content)
        with open(to_path, mode='wb') as f:
            f.write(bytes(content_unix))
        return self.success(to_path)
