from django.db import models
from users.models import *
from products.models import *
# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="주문자")
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, verbose_name="상품")
    paymentMethod = models.CharField(max_length=30, verbose_name="지불방식")
    destination = models.CharField(max_length=200, verbose_name="배송주소")
    orderDateTime = models.DateTimeField(default=timezone.now)