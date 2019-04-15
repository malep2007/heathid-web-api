from django.db import models
from healthid.apps.orders.models import Suppliers
from taggit.managers import TaggableManager


class ProductCategory(models.Model):
    name = models.CharField(max_length=50)


class MeasurementUnit(models.Model):
    name = models.CharField(max_length=50)


class Product(models.Model):
    product_category = models.ForeignKey(
        ProductCategory, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=244, unique=True)
    measurement_unit = models.ForeignKey(
        MeasurementUnit, on_delete=models.CASCADE)
    pack_size = models.CharField(max_length=50)
    sku_number = models.CharField(max_length=100, null=False)
    is_approved = models.BooleanField(default=False)
    description = models.CharField(max_length=150)
    brand = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50)
    vat_status = models.CharField(max_length=50)
    quality = models.CharField(max_length=50)
    sales_price = models.IntegerField()
    created_date = models.DateField(auto_now=True, auto_now_add=False)
    nearest_expiry_date = models.DateField(
        auto_now=False, auto_now_add=False, null=True)
    prefered_supplier = models.ForeignKey(
        Suppliers, related_name='prefered', on_delete=models.CASCADE)
    backup_supplier = models.ForeignKey(
        Suppliers, related_name='backup', on_delete=models.CASCADE)
    tags = TaggableManager()

    @property
    def get_tags(self):
        return self.tags.all()

    def __str__(self):
        return self.product_name