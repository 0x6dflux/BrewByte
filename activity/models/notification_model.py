from django.contrib.auth import get_user_model
from django.db import models

from activity.models import CommentModel
from general.models import BaseModel
from sale.models import OrderModel

AUTH_USER = get_user_model()


class NotificationModel(BaseModel):
    responsible_user_id = models.ForeignKey(AUTH_USER, models.CASCADE, related_name="notification_responsible_user_id")
    order_id = models.ForeignKey(OrderModel, models.CASCADE, null=True, blank=True)
    comment_id = models.ForeignKey(CommentModel, models.CASCADE, null=True, blank=True)
    description = models.TextField()
    is_seen = models.BooleanField()
