import xlwt
from django.http import HttpResponse


class ExcelWrite:
    def __init__(self, sheet_name: str):
        self.wb = xlwt.Workbook(encoding='utf-8')
        self.sheet = self.wb.add_sheet(sheet_name)
        self.response = HttpResponse(content_type='application/vnd.ms-excel')
        self.response['Content-Disposition'] = 'attachment; filename=%s.xls' % sheet_name

    def write_header(self, header_list: list):
        """
        写入表头
        :param header_list: 表头列表
        :return:
        """
        for i in range(len(header_list)):
            self.sheet.write(0, i, header_list[i])

    def write_data(self, data_list: list):
        """
        写入数据
        :param data_list: 数据列表
        :return:
        """
