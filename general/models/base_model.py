# from django.contrib.auth import get_user_model
from django.conf import settings
from django.db import models


AUTH_USER = settings.AUTH_USER_MODEL
# AUTH_USER = get_user_model()


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(AUTH_USER, models.CASCADE,null=True, blank=True,related_name="created_%(class)ss")
    updated_by = models.ForeignKey(AUTH_USER, models.CASCADE, null=True, blank=True,related_name="updated_%(class)ss")

    class Meta:
        abstract = True


