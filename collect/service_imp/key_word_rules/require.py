# -*- coding: utf-8 -*-
"""
@Time: 2021/6/28 15:49
@Author: zzhang zzhang@cenboomh.com
@File: require.py
@desc:
"""
from collect.collect_service import CollectService


class Require(CollectService):
    def __init__(self, op_user=None):
        """
        引入文件
        """
        CollectService.__init__(self, op_user)

    def handler(self, template, sql_file_content, params, config_rule, config_dir):
        import re
        require_sql_list = re.findall(config_rule["reg"], sql_file_content)
        for require_sql in require_sql_list:
            if not require_sql:
                continue
            require_sql_file_name = require_sql.replace("\"", "").replace("'", "").strip()
            require_sql_path = config_dir + "/" + require_sql_file_name
            import os
            if not os.path.exists(require_sql_path):
                self.log(require_sql + "不存在", "error")
                return self.fail("依赖文件 " + require_sql + "文件不存在")
            with open(require_sql_path, 'r') as f:
                require_sql_file_content = f.read()
            sql_file_content = sql_file_content.replace("require({require_sql})".format(require_sql=require_sql),
                                                        require_sql_file_content)

        return self.success(sql_file_content)
