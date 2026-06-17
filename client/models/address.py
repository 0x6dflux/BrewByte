from django.db import models
from client.models import CustomerProfile, ManagerProfile

class Address(models.Model):
    name = models.CharField(max_length=50)
    postal_address = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    customer_profile = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE , blank=True, null=True)
    manager_profile = models.ForeignKey(ManagerProfile, on_delete=models.CASCADE , blank=True, null=True)

    
