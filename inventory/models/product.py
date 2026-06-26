from django.db import models

from general.models import BaseModel


class Product(BaseModel):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    average_score = models.FloatField(default=0.0)
    inventory_stock = models.IntegerField(default=0)
    sale_stock = models.IntegerField(default=0)
    category_id = models.ForeignKey("inventory.Category", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name}"
