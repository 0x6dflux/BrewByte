from django.contrib.auth import get_user_model
from django.db import models

from client.models import Address
from general.models import BaseModel
from sale.models import CartModel, DiscountModel

# import ProductModel

AUTH_USER = get_user_model()


class OrderModel(BaseModel):
    cart_id = models.ForeignKey(CartModel, models.CASCADE)
    user_id = models.ForeignKey(AUTH_USER, models.CASCADE)
    address_id = models.ForeignKey(Address, models.CASCADE)
    discount_id = models.ForeignKey(DiscountModel, models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=1)
    tax = models.DecimalField(max_digits=10, decimal_places=1)
    taxed_amount = models.DecimalField(max_digits=10, decimal_places=1)
    is_active = models.BooleanField(default=True, db_default=True)
    is_approved = models.BooleanField(default=False, db_default=False)



class OrderItemModel(BaseModel):
    order_id = models.ForeignKey(OrderModel, models.CASCADE)
    # product_id = models.ForeignKey(ProductModel, models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=1)
    price = models.DecimalField(max_digits=10, decimal_places=1)
    amount = models.DecimalField(max_digits=10, decimal_places=1)
