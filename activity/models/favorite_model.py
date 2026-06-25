from django.contrib.auth import get_user_model
from django.db import models

from general.models import BaseModel
from inventory.models import Product

AUTH_USER = get_user_model()


class FavoriteModel(BaseModel):
    user_id = models.ForeignKey(AUTH_USER, models.CASCADE)
    product_id = models.ForeignKey(Product, models.CASCADE)

    def __str__(self) -> str:
        return f"FV{self.pk}-{self.product_id.name}-{self.user_id.first_name}-{self.user_id.last_name}"
