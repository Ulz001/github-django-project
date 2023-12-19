from django.core.validators import MinValueValidator
from django.db import models


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


class OutInventory(models.Model):
    """
    出库表
    """
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name='OutInventory',
                                 verbose_name='物料序号')
    out_way = models.CharField(max_length=8, null=False, verbose_name='去向途径')
    out_datatime = models.DateTimeField(auto_now=True, verbose_name='出库时间')
    supplier = models.CharField(max_length=20, null=False, verbose_name='消耗单位')
    num = models.IntegerField(null=False, verbose_name='出库数量', validators=[MinValueValidator(0)])


class CheckInventory(models.Model):
    """
    盘点表
    """
    material = models.ForeignKey(Material, on_delete=models.CASCADE, verbose_name='物料序号',
                                 related_name='CheckInventory')
    datetime = models.DateTimeField(auto_now_add=True, verbose_name='盘点日期')
    num = models.IntegerField(null=False, verbose_name='库存数量')
    actual_num = models.IntegerField(null=False, verbose_name='实际数量')
