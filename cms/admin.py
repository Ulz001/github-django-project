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
    actions = ['export_materials', ]

    def export_materials(self, request, queryset):
        return export_excel.ExcelWrite(sheet_name='物料清单', queryset=queryset).write_header.write_data()

    export_materials.short_description = "导出物料清单"
    export_materials.icon = "fas fa-file-excel"
    export_materials.type = "success"


@admin.register(InInventory)
class InInventoryAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'material', 'num', 'source', 'in_datetime', 'in_supplier',
    )
    list_filter = ('id', 'source', 'in_datetime')
    actions = ['export_excel', ]

    def export_excel(self, request, queryset):
        excel = export_excel.ExcelWrite(sheet_name='入库单据', queryset=queryset).write_header.write_data()
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
    actions = ['export_out', ]

    def export_out(self, request, queryset):
        return export_excel.ExcelWrite(sheet_name='出库单据', queryset=queryset).write_header.write_data()

    export_out.short_description = "导出选中单据"
    export_out.type = "success"
    export_out.icon = "fas fa-file-excel"


@admin.register(CheckInventory)
class CheckInventoryAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'num', 'actual_num', 'datetime'
    )
    list_filter = ('id', 'datetime')
    actions = ['export_check', ]

    def export_check(self, request, queryset):
        return export_excel.ExcelWrite(sheet_name='盘点记录', queryset=queryset).write_header.write_data()

    export_check.short_description = "导出选中单据"
    export_check.type = "success"
    export_check.icon = "fas fa-file-excel"

    export_check.short_description = "导出选中单据"
    export_check.type = "success"
    export_check.icon = "fas fa-file-excel"
