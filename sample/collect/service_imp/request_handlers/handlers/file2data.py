# -*- coding: utf-8 -*-

from collect.service_imp.request_handlers.request_handler import RequestHandler
from collect.utils.collect_utils import get_safe_data


class File2data(RequestHandler):
    """
     文件转内容
    """
    fc_const = {
        "file_field_name": "file_field",
        "accept_type_name": "accept_type",
        "forbid_type_name": "forbid_type",
        "to_list_name": "to_list",
    }

    def get_accept_type_name(self):
        return self.fc_const["accept_type_name"]

    def get_to_list_name(self):
        return self.fc_const["to_list_name"]

    def get_forbid_type_name(self):
        return self.fc_const["forbid_type_name"]

    def get_file_field_name(self):
        return self.fc_const["file_field_name"]

    def handler(self, params, config, template):
        file_field_name = get_safe_data(self.get_file_field_name(), config)
        if not file_field_name:
            return self.fail(self.get_file_field_name() + "字段配置不存在")
        request = self.get_request(template)
        file_list = request.FILES.getlist(file_field_name)
        if not file_list:
            return self.fail("上传文件不存在")
        accept_type_name = get_safe_data(self.get_accept_type_name(), config, "")
        accept_type = get_safe_data(accept_type_name, params, "").split(",")
        forbid_type_type = get_safe_data(self.get_forbid_type_name(), config, "")
        forbid_type = get_safe_data(forbid_type_type, params, "").split(",")

        # 检查是否通过格式校验
        for file in file_list:
            file_name = file.name
            expanded_name = "." + file_name.split(".")[-1]
            if forbid_type and expanded_name in forbid_type:
                return self.fail(msg="文件上传不支持【{0}】类文件！！！".format(expanded_name))
            if accept_type and expanded_name not in accept_type:
                return self.fail(msg="文件上传不支持【{0}】类文件！！！".format(expanded_name))
            if file.size > 1024 * 1024 * 1024 * 100:
                return self.fail(msg="上传【{0}】文件,不能大于100M！！！".format(file_name))
        # 读取文件内容
        to_list = True

        if self.get_to_list_name() in config:
            to_list = config[self.get_to_list_name()]

        data_list = []
        if to_list:
            for file in file_list:
                item = {
                    "data": file.read(),
                    "name": file.name,
                    "size": file.size,

                }
                data_list.append(item)
        else:
            if len(file_list)>0:
                data_list = file_list[0].read()
                data_list= bytes(data_list)


        save_field = get_safe_data(self.get_save_field_name(), config)
        if save_field:
            params[save_field] = data_list

        del params[file_field_name]
        return self.success(params)
