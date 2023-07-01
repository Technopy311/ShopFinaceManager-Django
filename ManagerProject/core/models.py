from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField("Product Name", default="Product", max_length=200)
    price = models.IntegerField("Product Price", default=0)
    stock = models.IntegerField("Product Stock", default=0)