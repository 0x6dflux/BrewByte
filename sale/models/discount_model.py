from django.db import models

from general.models import BaseModel
from django.contrib.auth.models import User


class DiscountModel(BaseModel):
    user_id = models.ForeignKey(User)
    expire_datetime = models.DateTimeField()
    code = models.CharField()
    percent = models.IntegerField()
    max_amount = models.DecimalField(max_digits=10, decimal_places=1)
    order_min_amount = models.DecimalField(max_digits=10, decimal_places=1)
