from django.conf import settings
from django.db import models

from general.models import BaseModel

AUTH_USER = settings.AUTH_USER_MODEL


class DiscountModel(BaseModel):
    user_id = models.ForeignKey(AUTH_USER, models.CASCADE)
    expire_datetime = models.DateTimeField()
    code = models.CharField(max_length=5)
    percent = models.IntegerField()
    max_amount = models.DecimalField(max_digits=10, decimal_places=1)
    order_min_amount = models.DecimalField(max_digits=10, decimal_places=1)

    def __str__(self) -> str:
        return f"DC{self.pk}-{self.code}"
