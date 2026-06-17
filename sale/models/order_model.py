from django.contrib.auth.models import User
from django.db import models

from general.models import BaseModel
from sale.models import CartModel, DiscountModel

# import AddressModel


# Create your models here.
class OrderModel(BaseModel):
    cart_id = models.ForeignKey(CartModel)
    user_id = models.ForeignKey(User)
    address_id = models.ForeignKey(AddressModel)
    discount_id = models.ForeignKey(DiscountModel)
    total_amount = models.DecimalField(max_digits=10, decimal_places=1)
    tax = models.DecimalField(max_digits=10, decimal_places=1)
    taxed_amount = models.DecimalField(max_digits=10, decimal_places=1)
