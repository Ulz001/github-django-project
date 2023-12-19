import xlwt
from django.http import HttpResponse


class ExcelWrite:
    def __init__(self, sheet_name: str, queryset):
        """
        :param sheet_name: 文件名称
        :param queryset: 数据
        """
        self.wb = xlwt.Workbook(encoding='utf-8')
        self.sheet = self.wb.add_sheet(sheet_name)
        self.response = HttpResponse(content_type='application/vnd.ms-excel')
        self.style = xlwt.XFStyle()
        self.alignment = xlwt.Alignment()
        self.alignment.horz = xlwt.Alignment.HORZ_CENTER
        self.alignment.vert = xlwt.Alignment.VERT_CENTER
        self.style.alignment = self.alignment
        self.font = xlwt.Font()
        self.font.name = '宋体'
        self.font.bold = True
        self.font.height = 200
        self.style.font = self.font
        self.col = 0
        self.row = 1
        self.in_obj = 0
        self.queryset = queryset
        self.headers = list(self.queryset.values()[0].keys())

    @property
    def write_header(self):
        """
        写入表头
        :param
        :return: None
        """
        for i in range(len(self.headers)):
            self.sheet.write(0, i, self.headers[i], self.style)
        return self

    def write_data(self):
        """
        :return:
        """
        for data in self.queryset.values():
            for header in self.headers:
                if header == 'material_id':
                    print(self.queryset[self.in_obj])
                    self.sheet.write(self.row, self.col, str(self.queryset[self.in_obj]), self.style)
                else:
                    self.sheet.write(self.row, self.col, data[header], self.style)
                self.col += 1
            self.row += 1
            self.col = 0
            self.in_obj += 1
        self.wb.save(self.response)
        return self.response
