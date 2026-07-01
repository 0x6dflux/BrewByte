from django.db import models

from general.models import BaseModel
from inventory.models import Product


class OrderItemModel(BaseModel):
    order_id = models.ForeignKey(
        "sale.OrderModel",
        models.CASCADE,
        null=True,
        blank=True,
    )
    product_id = models.ForeignKey(
        Product,
        models.CASCADE,
        null=True,
        blank=True,
    )
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"OI{self.pk}-{self.product_id.name}"

    def save(self):
        self.amount = self.quantity * self.price
        return super().save()
