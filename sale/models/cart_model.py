from decimal import Decimal

from django.conf import settings
from django.db import models

from general.models import BaseModel

AUTH_USER = settings.AUTH_USER_MODEL


class CartModel(BaseModel):
    user_id = models.ForeignKey(AUTH_USER, models.CASCADE)
    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal(0.0),
    )
    is_active = models.BooleanField(default=True, db_default=True)

    def __str__(self) -> str:
        return f"CR{self.pk}-{self.user_id.first_name}-{self.user_id.last_name}"
