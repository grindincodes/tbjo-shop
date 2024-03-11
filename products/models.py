from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=200)
    img = models.ImageField(upload_to='img/', blank=False)
    price = models.IntegerField(default=0, validators=[MinValueValidator(0, MaxValueValidator(10000000))])
    registeredDateTime = models.DateTimeField(default=timezone.now)