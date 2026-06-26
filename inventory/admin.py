from django.contrib import admin

from inventory.models import (
    Category,
    Ingredient,
    ProductPicture,
    Product,
)

admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(ProductPicture)
admin.site.register(Product)
