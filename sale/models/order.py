from decimal import Decimal

from django.contrib.auth import get_user_model
from django.db import models

from client.models import Address
from general.models import BaseModel
from inventory.models import Product
from sale.models import CartModel, DiscountModel

AUTH_USER = get_user_model()


class OrderModel(BaseModel):
    cart_id = models.ForeignKey(CartModel, models.CASCADE)
    user_id = models.ForeignKey(AUTH_USER, models.CASCADE)
    address_id = models.ForeignKey(Address, models.CASCADE)
    discount_id = models.ForeignKey(DiscountModel, models.CASCADE)
    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=1,
        default=Decimal(0.0),
    )
    tax = models.DecimalField(max_digits=10, decimal_places=1)
    taxed_amount = models.DecimalField(
        max_digits=10,
        decimal_places=1,
        default=Decimal(0.0),
    )

    def __str__(self) -> str:
        return f"OR{self.pk}-{self.user_id.first_name}-{self.user_id.last_name}"


class OrderItemModel(BaseModel):
    order_id = models.ForeignKey(OrderModel, models.CASCADE, null=True, blank=True)
    product_id = models.ForeignKey(Product, models.CASCADE, null=True, blank=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=1)
    price = models.DecimalField(max_digits=10, decimal_places=1)
    amount = models.DecimalField(max_digits=10, decimal_places=1)

    def __str__(self) -> str:
        return f"OI{self.pk}-{self.product_id.name}"
