from django.db import models
from client.models import CustomerProfile, ManagerProfile

from general.models import BaseModel

class Address(BaseModel):
    name = models.CharField(max_length=50)
    postal_address = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    customerprofile_id = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE , blank=True, null=True)
    managerprofile_id = models.ForeignKey(ManagerProfile, on_delete=models.CASCADE , blank=True, null=True)
    

    
