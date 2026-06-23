from django.db import models
from inventory.models import product

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    product_id = models.ForeignKey(product, on_delete=models.CASCADE, blank=True, null=True)




