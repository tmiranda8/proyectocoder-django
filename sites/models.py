from django.db import models
from datetime import date
len=32
class NetworkDevice(models.Model):
    def __str__(self):
        return f'{self.brand} {self.product_model}'
    brand = models.CharField(max_length=len)
    product_model = models.CharField(max_length=len)
    product_type = models.CharField(max_length=len)
    price = models.IntegerField(blank=True)
    description = models.TextField(blank=True)
    created = models.DateField(default=date.today)

class IoTDevice(models.Model):
    def __str__(self):
        return f'{self.brand} {self.product_model}'
    brand = models.CharField(max_length=len)
    product_model = models.CharField(max_length=len)
    product_type = models.CharField(max_length=len)
    price = models.IntegerField(blank=True)
    description = models.TextField(blank=True)
    created = models.DateField(default=date.today)
    class Meta:
        verbose_name = "IoT Device"

class HardwareComponent(models.Model):
    def __str__(self):
        return f'{self.brand} {self.product_model}'
    brand = models.CharField(max_length=len)
    product_model = models.CharField(max_length=len)
    product_type = models.CharField(max_length=len)
    price = models.IntegerField(blank=True)
    description = models.TextField(blank=True)
    created = models.DateField(default=date.today)

class GlobalSearch(models.Model):
    identifier = models.TextField()