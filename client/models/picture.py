from django.db import models
from client.models import CustomerProfile, ManagerProfile

class Picture(models.Model):
    file_path = models.FilePathField(null=True, blank=True)
    customer_profile = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE , blank=True, null=True)
    manager_profile = models.ForeignKey(ManagerProfile, on_delete=models.CASCADE , blank=True, null=True)

