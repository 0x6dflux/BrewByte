from django.contrib.auth.models import User
from django.db import models

from general.models import BaseModel
from sale.models import CartModel, DiscountModel, OrderModel

# import ProductModel


# Create your models here.
class OrderItemModel(BaseModel):
    order_id = models.ForeignKey(OrderModel)
    product_id = models.ForeignKey(ProductModel)
    quantity = models.DecimalField(max_digits=10, decimal_places=1)
    price = models.DecimalField(max_digits=10, decimal_places=1)
    amount = models.DecimalField(max_digits=10, decimal_places=1)
