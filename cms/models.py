from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.html import format_html


class Material(models.Model):
    """
    物料表
    """
    name = models.CharField(max_length=15, null=False, unique=True, verbose_name='物料名称')
    max_inventory = models.IntegerField(null=False, validators=[MinValueValidator(1)], verbose_name='最大库存')
    min_inventory = models.IntegerField(null=False, validators=[MinValueValidator(1)], verbose_name='最小库存')
    now_inventory = models.IntegerField(null=False, validators=[MinValueValidator(0)], verbose_name='当前库存')
    description = models.CharField(max_length=100, null=True, verbose_name='物料描述')
    picture = models.ImageField(upload_to='media/upload_images', null=True, verbose_name='物料图片')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, verbose_name='物料价格')
    now_datetime = models.DateTimeField(auto_now=True, verbose_name='入库时间')
    supplier = models.CharField(max_length=15, null=False, verbose_name='供应商')

    def image(self):
        if not self.picture:
            return '无图片'
        return format_html("""<div><img src='{}' style='width:50px;height:50px;' ></div>""", self.picture.url)

    image.short_description = '图片'

    def warning(self, obj):
        if obj.now_inventory < obj.min_inventory:
            return format_html('<span style="color:red;">库存不足,请及时补货</span>')
        elif obj.now_inventory > obj.max_inventory:
            return format_html('<span style="color:blue;">库存超出，不允许入库</span>')

    warning.short_description = '库存警告'

    def clean(self):
        if self.max_inventory < self.min_inventory:
            raise ValidationError('最大库存不能小于最小库存')

    class Meta:
        verbose_name = '物料'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class InInventory(models.Model):
    """
    入库表
    """
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name='InInventory',
                                 verbose_name='物料名称')
    num = models.IntegerField(null=False, validators=[MinValueValidator(1)], verbose_name='入库数量')
    source = models.CharField(max_length=10, null=False, verbose_name='来源')
    in_datetime = models.DateTimeField(auto_now=True, verbose_name='入库时间')
    in_supplier = models.CharField(max_length=15, verbose_name='供应商')

    class Meta:
        verbose_name = '入库'
        verbose_name_plural = verbose_name


class OutInventory(models.Model):
    """
    出库表
    """
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name='OutInventory',
                                 verbose_name='物料序号')
    out_way = models.CharField(max_length=8, null=False, verbose_name='去向途径')
    out_datetime = models.DateTimeField(auto_now=True, verbose_name='出库时间')
    supplier = models.CharField(max_length=20, null=False, verbose_name='消耗单位')
    num = models.IntegerField(null=False, verbose_name='出库数量', validators=[MinValueValidator(0)])

    class Meta:
        verbose_name = '出库'
        verbose_name_plural = verbose_name


class CheckInventory(models.Model):
    """
    盘点表
    """
    material = models.ForeignKey(Material, on_delete=models.CASCADE, verbose_name='物料序号',
                                 related_name='CheckInventory')
    datetime = models.DateTimeField(auto_now_add=True, verbose_name='盘点日期')
    num = models.IntegerField(null=False, verbose_name='库存数量')
    actual_num = models.IntegerField(null=False, verbose_name='实际数量')
