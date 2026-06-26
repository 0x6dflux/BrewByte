from django.db import models
from django.conf import settings

from general.models import BaseModel
from inventory.models import Product


AUTH_USER = settings.AUTH_USER_MODEL


class CommentModel(BaseModel):
    class Score(models.IntegerChoices):
        GREAT = 5
        VERY_GOOD = 4
        GOOD = 3
        POOR = 2
        BAD = 1

    user_id = models.ForeignKey(AUTH_USER, models.CASCADE)
    responsible_user_id = models.ForeignKey(
        AUTH_USER,
        models.CASCADE,
        related_name="comment_responsible_user_id",
    )
    product_id = models.ForeignKey(Product, models.CASCADE)
    is_bought = models.BooleanField(default=False, db_default=False)
    description = models.TextField()
    score = models.IntegerField(choices=Score)
    is_approved = models.BooleanField(default=False, db_default=False)

    def __str__(self) -> str:
        return f"CM{self.pk}-{self.product_id.name}-{self.responsible_user_id.first_name}-{self.responsible_user_id.last_name}"
