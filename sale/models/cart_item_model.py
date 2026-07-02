from decimal import Decimal

from django.db import models

from general.models import BaseModel
from inventory.models import Product


class CartItemModel(BaseModel):
    product_id = models.ForeignKey(Product, models.CASCADE, null=True, blank=True)
    cart_id = models.ForeignKey(
        "sale.CartModel",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(db_default=0, default=0)
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        db_default=Decimal("0"),
        default=Decimal("0"),
    )  # price * quantity

    def __str__(self) -> str:
        return f"CI{self.pk}-{self.product_id.name}"
