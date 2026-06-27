from decimal import Decimal

from django.conf import settings
from django.db import models

from client.models import Address
from general.models import BaseModel
from sale.models import CartModel, DiscountModel

AUTH_USER = settings.AUTH_USER_MODEL


class OrderModel(BaseModel):
    cart_id = models.ForeignKey(CartModel, models.CASCADE)
    user_id = models.ForeignKey(AUTH_USER, models.CASCADE)
    address_id = models.ForeignKey(
        Address,
        models.CASCADE,
        null=True,
        blank=True,
    )
    discount_id = models.ForeignKey(
        DiscountModel,
        models.CASCADE,
        null=True,
        blank=True,
    )
    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=1,
        default=Decimal(0.0),
    )
    discount = models.DecimalField(
        max_digits=10,
        decimal_places=1,
        null=True,
        blank=True,
    )
    discounted_amount = models.DecimalField(
        max_digits=10,
        decimal_places=1,
        null=True,
        blank=True,
    )
    tax = models.DecimalField(
        max_digits=10,
        decimal_places=1,
        null=True,
        blank=True,
    )
    taxed_amount = models.DecimalField(
        max_digits=10,
        decimal_places=1,
        default=Decimal(0.0),
    )
    is_active = models.BooleanField(default=True, db_default=True)
    is_approved = models.BooleanField(default=False, db_default=False)

    def __str__(self) -> str:
        return f"OR{self.pk}-{self.user_id.first_name}-{self.user_id.last_name}"
