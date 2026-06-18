from django.db import models

from general.models import BaseModel
#from sale.models import CartModel
from sale.models.cart_model import CartModel
# import ProductModel


# Create your models here.
class CartItemModel(BaseModel):
    product_id = models.ForeignKey(ProductModel)
    cart_id = models.ForeignKey(CartModel)
    price = models.DecimalField(max_digits=10, decimal_places=1)
    quantity = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=1)  # price * quantity
