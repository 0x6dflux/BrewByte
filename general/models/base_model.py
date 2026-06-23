from django.contrib.auth import get_user_model
from django.db import models

AUTH_USER = get_user_model()


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(AUTH_USER, models.CASCADE)
    updated_by = models.ForeignKey(AUTH_USER, models.CASCADE, null=True, blank=True)
