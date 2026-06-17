from django.db import models
from client.models import CustomUser

class Picture(models.Model):
    file_path = models.FilePathField(null=True, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE , blank=True, null=True)