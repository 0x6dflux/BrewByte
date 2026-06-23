from django.db import models
from client.models import CustomerProfile, ManagerProfile
#from client.models import User
class Picture(models.Model):
    file_path = models.ImageField(upload_to='profiles/', null=True, blank=True)
    customerprofile_id = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE, blank=True, null=True)
    managerprofile_id = models.ForeignKey(ManagerProfile, on_delete=models.CASCADE, blank=True, null=True)
