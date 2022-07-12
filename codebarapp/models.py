from django.db import models

# Create your models here.

class Product(models.Model):
    productName = models.CharField(max_length=100)
    brand = models.CharField(max_length=100, null=True,blank=True)
    codebar = models.CharField(max_length=100, unique=True)
    ref = models.CharField(max_length=100)