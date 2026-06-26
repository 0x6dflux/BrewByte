from django.db import models
from django.conf import settings

from general.models import BaseModel

AUTH_USER = settings.AUTH_USER_MODEL


class ClientPicture(BaseModel):
    file_path = models.ImageField(upload_to="clients/")
    user_id = models.ForeignKey(
        AUTH_USER,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.pk
