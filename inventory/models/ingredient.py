from django.db import models
from general.models import BaseModel

class Ingredient(BaseModel):
    name = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    product_id = models.ForeignKey('inventory.Product', on_delete=models.CASCADE, blank=True, null=True)

