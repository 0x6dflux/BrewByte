from django.db import models
from client.models import CustomUser

class ManagerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    graduated_date = models.DateField(null=True, blank= True)
    national_code = models.CharField(max_length=10, null=True, blank=True)
    birth_date = models.DateField(blank=True, null=True)