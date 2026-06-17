from django.db import models
from client.models import CustomUser

class Address(models.Model):
    name = models.CharField(max_length=50)
    postal_address = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE , blank=True, null=True)
    

    
