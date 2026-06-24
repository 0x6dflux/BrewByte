from django.db import models

from client.models import CustomerProfile, ManagerProfile
from general.models import BaseModel

class ClientPicture(BaseModel):
    file_path = models.FilePathField(null=True, blank=True)
    customerprofile_id = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE , blank=True, null=True)
    managerprofile_id = models.ForeignKey(ManagerProfile, on_delete=models.CASCADE , blank=True, null=True)