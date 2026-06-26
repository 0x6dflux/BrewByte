from django.db import models

from client.models import CustomerProfile, ManagerProfile
from general.models import BaseModel
from django.contrib.auth import get_user_model

AUTH_USER = get_user_model()

class ClientPicture(BaseModel):
    file_path = models.FilePathField(null=True, blank=True)
    user_id = models.ForeignKey(AUTH_USER, on_delete=models.CASCADE , blank=True, null=True)

    def __str__(self):
        return self.pk