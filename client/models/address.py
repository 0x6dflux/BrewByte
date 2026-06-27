from django.conf import settings
from django.db import models

from general.models import BaseModel

AUTH_USER = settings.AUTH_USER_MODEL


class Address(BaseModel):
    name = models.CharField(max_length=50)
    postal_address = models.CharField(max_length=200)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    user_id = models.ForeignKey(
        AUTH_USER, on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return self.name
