from django.db import models
from client.models import CustomerProfile, ManagerProfile
from django.contrib.auth import get_user_model

from general.models import BaseModel
AUTH_USER = get_user_model()

class Address(BaseModel):
    name = models.CharField(max_length=50)
    postal_address = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    user_id = models.ForeignKey(AUTH_USER, on_delete=models.CASCADE , blank=True, null=True)

    def __str__(self):
        return self.name

    
