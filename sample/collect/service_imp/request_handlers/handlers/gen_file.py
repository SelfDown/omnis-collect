# -*- coding: utf-8 -*-

from collect.service_imp.request_handlers.request_handler import RequestHandler
from collect.utils.collect_utils import get_safe_data


class GenFile(RequestHandler):
    """
     文件转内容
    """
    gf_const = {
        "item_name": "item",
        "file_name_name": "file_name",
        "file_content_name": "file_content",
        "dir_path_name": "dir_path",

    }

    def get_item_name(self):
        return self.gf_const["item_name"]

    def get_file_content_name(self):
        return self.gf_const["file_content_name"]

    def get_dir_path_name(self):
        return self.gf_const["dir_path_name"]

    def get_file_name_name(self):
        return self.gf_const["file_name_name"]

    def handler(self, params, config, template):

        foreach_name = get_safe_data(self.get_foreach_name(), config)
        if not foreach_name:
            return self.fail("配置中没有找到" + self.get_foreach_name() + "字段")

        file_list = get_safe_data(foreach_name, params)
        item_name = get_safe_data(self.get_item_name(), config)

        file_name_name = get_safe_data(self.get_file_name_name(), config)
        file_content_name = get_safe_data(self.get_file_content_name(), config)
        params_result = self.get_params_result(template)

        from collect.service_imp.common.filters.template_tool import TemplateTool
        tool = TemplateTool(op_user=self.op_user)

        file_dir_name = get_safe_data(self.get_dir_path_name(), config)
        file_dir = self.get_render_data(file_dir_name, params_result, tool)
        import os
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        data_list = []
        # 生成文件
        for item in file_list:
            params_result[item_name] = item
            file_name = self.get_render_data(file_name_name, params_result, tool)
            file_path = file_dir + "/" + file_name
            parent_dir = os.path.dirname(file_path)
            if not os.path.exists(parent_dir):
                os.makedirs(parent_dir)
            with open(file_path, "wb") as f:
                file_content = self.get_render_data(file_content_name, params_result, tool)
                f.write(file_content)
            data_list.append(file_path)
        # 处理压缩
        import shutil
        try:
            dest = shutil.make_archive(file_dir, "zip", file_dir)
        except Exception as e:
            return self.fail(str(e))
        save_field = get_safe_data(self.get_save_field_name(), config)
        if save_field:
            params_result[save_field] = dest
        return self.success(params)
