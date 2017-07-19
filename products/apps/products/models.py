from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 100)
    weight = models.DecimalField(max_digits = 7, decimal_places = 3)
    price = models.DecimalField(max_digits = 7, decimal_places = 2)
    category = models.CharField(max_length = 20)
