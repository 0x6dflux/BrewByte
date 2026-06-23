from django.contrib.auth import get_user_model
from django.db import models

from general.models import BaseModel
from inventory.models import Product

AUTH_USER = get_user_model()


class FavoriteModel(BaseModel):
    user_id = models.ForeignKey(AUTH_USER, models.CASCADE)
    product_id = models.ForeignKey(Product, models.CASCADE)
