from django.db import models
from general.models import BaseModel

class Picture(BaseModel):
    file_path = models.ImageField(upload_to='products/') 
    product_id = models.ForeignKey('inventory.Product', on_delete=models.CASCADE)
