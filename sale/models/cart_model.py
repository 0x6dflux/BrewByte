from django.db import models

from general.models import BaseModel
from django.contrib.auth.models import User


# Create your models here.
class CartModel(BaseModel):
    user_id = models.ForeignKey(User)
    total_amount = models.DecimalField(max_digits=10, decimal_places=1)
