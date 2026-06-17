from django.db import models
from client.models import CustomUser


class CustomerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    birth_date = models.DateField(blank=True, null=True)
    