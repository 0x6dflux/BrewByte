from django.db import models

from general.models import BaseModel


class ProductPicture(BaseModel):
    file_path = models.ImageField(upload_to="products/")
    product_id = models.ForeignKey("inventory.Product", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"PIC{self.pk}-{self.product_id.name}"
