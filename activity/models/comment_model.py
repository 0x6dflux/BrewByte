from django.contrib.auth import get_user_model
from django.db import models

from general.models import BaseModel
from inventory.models import Product

AUTH_USER = get_user_model()


class CommentModel(BaseModel):
    user_id = models.ForeignKey(AUTH_USER, models.CASCADE)
    responsible_user_id = models.ForeignKey(
        AUTH_USER,
        models.CASCADE,
        related_name="comment_responsible_user_id",
    )
    product_id = models.ForeignKey(Product, models.CASCADE)
    is_bought = models.BooleanField()
    description = models.TextField()
    score = models.IntegerField()
    is_approved = models.BooleanField()

    def __str__(self) -> str:
        return f"CM{self.pk}-{self.product_id.name}-{self.responsible_user_id.first_name}-{self.responsible_user_id.last_name}"
