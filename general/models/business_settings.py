from django.contrib.auth import get_user_model
from django.db import models

from general.models.base_model import BaseModel

AUTH_USER = get_user_model()


class BusinessSetting(BaseModel):
    deafult_comment_responsible_user_id = models.ForeignKey(
        AUTH_USER,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="deafult_comment_responsible_user_id",
    )
    deafult_notification_responsible_user_id = models.ForeignKey(
        AUTH_USER,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="deafult_notification_responsible_user_id",
    )

    def __str__(self) -> str:
        return f"BS{self.pk}"
