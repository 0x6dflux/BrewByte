from django.conf import settings
from django.db import models

from general.models import BaseModel
from inventory.models import Product

AUTH_USER = settings.AUTH_USER_MODEL


class FavoriteModel(BaseModel):
    user_id = models.ForeignKey(AUTH_USER, models.CASCADE)
    product_id = models.ForeignKey(Product, models.CASCADE)

    def __str__(self) -> str:
        return f"FV{self.pk}-{self.product_id.name}-{self.user_id.first_name}-{self.user_id.last_name}"
