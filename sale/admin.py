from django.contrib import admin

from sale.models import (
    CartItemModel,
    CartModel,
    DiscountModel,
    OrderItemModel,
    OrderModel,
)

admin.site.register(CartItemModel)
admin.site.register(CartModel)
admin.site.register(DiscountModel)
admin.site.register(OrderItemModel)
admin.site.register(OrderModel)
