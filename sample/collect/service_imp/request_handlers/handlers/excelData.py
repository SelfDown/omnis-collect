# -*- coding: utf-8 -*-

from collect.service_imp.request_handlers.request_handler import RequestHandler
from collect.utils.collect_utils import get_safe_data


class excelData(RequestHandler):
    """
     从数组中，取值
    """
    ed_const = {
        "file_field_name": "file_field",
        "sheets_name": "sheets",
        "sheet_index_name": "sheet_index",
        "start_row_name": "start_row",
        "start_col_name": "start_col",
        "fields_name": "fields",
        "must_name": "must",
    }

    def get_must_name(self):
        return self.ed_const["must_name"]

    def get_fields_name(self):
        return self.ed_const["fields_name"]

    def get_start_col_name(self):
        return self.ed_const["start_col_name"]

    def get_start_row_name(self):
        return self.ed_const["start_row_name"]

    def get_sheet_index_name(self):
        return self.ed_const["sheet_index_name"]

    def get_file_file_name(self):
        return self.ed_const["file_field_name"]

    def get_sheets_name(self):
        return self.ed_const["sheets_name"]

    def handler(self, params, config, template):
        file_field_name = get_safe_data(self.get_file_file_name(), config)
        if not file_field_name:
            return self.fail(self.get_file_file_name() + "字段配置不存在")
        f = get_safe_data(file_field_name, params)
        if not f:
            return self.fail("上传文件不存在")
        import xlrd as xlrd
        excel_type = f.name.split('.')[1]
        if excel_type not in ['xlsx', 'xls']:
            return self.fail("文件上传格式有误")
            # 开始解析上传的excel表格

        sheets = get_safe_data(self.get_sheets_name(), config)
        if not sheets:
            return self.fail(self.get_sheets_name() + "字段配置不存在")

        wb = xlrd.open_workbook(filename=None, file_contents=f.read())
        sheetsContent = wb.sheets()
        f.close()
        for sheet in sheets:
            sheetIndex = get_safe_data(self.get_sheet_index_name(), sheet, 0)
            startRow = get_safe_data(self.get_start_row_name(), sheet, 0)
            startCol = get_safe_data(self.get_start_col_name(), sheet, 0)
            if sheetIndex >= len(sheetsContent):
                return self.fail(str("excel 中第【" + sheetIndex) + "】个标签页不存在")

            fields = get_safe_data(self.get_fields_name(), sheet)
            if not fields:
                return self.fail(str("excel 中第【" + sheetIndex) + "】个标签页" + self.get_fields_name() + "配置不存在")
            table = sheetsContent[sheetIndex]
            dataList = []
            for rown in range(table.nrows):
                if rown < startRow:
                    continue
                item = {}
                append = True
                for index, field in enumerate(fields):
                    key = get_safe_data(self.get_key_name(), field)
                    must = get_safe_data(self.get_must_name(), field)
                    col = startCol + index
                    value = table.cell_value(rown, col)
                    if must and (value is None or value == ""):
                        append = False
                        break
                    item[key] = value
                if append:
                    dataList.append(item)
            save_field = get_safe_data(self.get_save_field_name(), sheet)
            if save_field:
                params[save_field] = dataList

        del params[file_field_name]
        return self.success(params)
