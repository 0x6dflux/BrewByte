from django.db import models
from django.conf import settings

from general.models.base_model import BaseModel


AUTH_USER = settings.AUTH_USER_MODEL


class BusinessSetting(BaseModel):
    default_comment_responsible_user_id = models.ForeignKey(
        AUTH_USER,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="default_comment_responsible_user_id",
    )
    default_notification_responsible_user_id = models.ForeignKey(
        AUTH_USER,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="default_notification_responsible_user_id",
    )
    default_tax_ratio = models.FloatField(default=10.0, db_default=10.0)

    def __str__(self) -> str:
        return f"BS{self.pk}"
