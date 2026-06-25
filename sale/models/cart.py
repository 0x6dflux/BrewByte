from django.contrib.auth import get_user_model
from django.db import models

from general.models import BaseModel
from inventory.models import Product

AUTH_USER = get_user_model()


class CartModel(BaseModel):
    user_id = models.ForeignKey(AUTH_USER, models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=1)

    def __str__(self) -> str:
        return f"CR{self.pk}-{self.user_id.first_name}-{self.user_id.last_name}"


class CartItemModel(BaseModel):
    product_id = models.ForeignKey(Product, models.CASCADE)
    cart_id = models.ForeignKey(CartModel, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=1)
    quantity = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=1)  # price * quantity

    def __str__(self) -> str:
        return f"CI{self.pk}-{self.product_id.name}"
