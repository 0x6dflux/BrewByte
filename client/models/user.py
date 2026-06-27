from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.core.exceptions import

from general.models import BaseModel


class User(AbstractUser, BaseModel):
    phone_number = models.CharField(max_length=14, unique=True)
    user_code = models.CharField(max_length=20, unique=True, blank=True)
    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    birthday = models.DateField(blank=True, null=True)
    is_customer = models.BooleanField(default=True, db_default=True)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["first_name", "last_name", "username", "email"]

    def __str__(self):
        return self.username
