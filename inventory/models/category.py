from django.db import models
from general.models import BaseModel

class Category(BaseModel):
    name = models.CharField(max_length=120)

















