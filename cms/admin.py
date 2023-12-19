from django.contrib import admin

from cms.models import Material, InInventory, OutInventory, CheckInventory

from cms.utils import export_excel

# 设置标题、页脚、login页面标题
admin.site.site_header = "商店库存管理系统"
admin.site.site_title = "商店库存管理系统"
admin.site.index_title = "商店库存管理系统"


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'image', 'name', 'max_inventory', 'min_inventory', 'now_inventory', 'description', 'price', 'supplier',
        'now_datetime', 'warning'
    )
    list_filter = ('id', 'name', 'supplier', 'now_datetime')


@admin.register(InInventory)
class InInventoryAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'material', 'num', 'source', 'in_datetime', 'in_supplier',
    )
    list_filter = ('id', 'source', 'in_datetime')
    actions = ['export_excel', ]

    def export_excel(self, request, queryset):
        excel = export_excel.ExcelWrite(sheet_name='入库单据', queryset=queryset).write_header.write_data()
        headers = list(queryset.values()[0].keys())
        rows = queryset.values()
        print(headers)
        print(rows)
        return excel

    export_excel.short_description = "导出选中单据"
    export_excel.icon = "fas fa-file-excel"
    export_excel.type = "success"


@admin.register(OutInventory)
class OutInventoryAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'material', 'num', 'out_way', 'out_datetime', 'supplier',
    )
    list_filter = ('id', 'out_way', 'out_datetime')


@admin.register(CheckInventory)
class CheckInventoryAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'num', 'actual_num', 'datetime'
    )
