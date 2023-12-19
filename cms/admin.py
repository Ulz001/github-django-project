from django.contrib import admin

from cms.models import Material, InInventory, OutInventory, CheckInventory

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
