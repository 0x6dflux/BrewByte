from django.db import models
from inventory.models import product

class Category(models.Model) :
    name = models.CharField(max_length=120)
    product_id = models.ForeignKey(product, on_delete=models.CASCADE, blank=True, null=True)




















