from django.contrib.auth import get_user_model
from django.db import models

from general.models import BaseModel

# import ProductModel

AUTH_USER = get_user_model()


class CartModel(BaseModel):
    user_id = models.ForeignKey(AUTH_USER, models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=1)


class CartItemModel(BaseModel):
    # product_id = models.ForeignKey(ProductModel)
    cart_id = models.ForeignKey(CartModel, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=1)
    quantity = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=1)  # price * quantity
