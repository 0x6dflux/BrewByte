from django.urls import path

from sale.views import (
    CreateOrder,
    UpdateOrderItem,
    FinalizeOrder,
    FinalizeDiscount,
    CheckInventory,
)


app_name = "sale"

urlpatterns = [
    path("order/new/", CreateOrder.as_view(), name="create_order"),
    path("order/new/update_item/", UpdateOrderItem.as_view(), name="update_order_item"),
    path(
        "order/new/check_inventory/", CheckInventory.as_view(), name="check_inventory"
    ),
    path("order/finalize/", FinalizeOrder.as_view(), name="finalize_order"),
    path(
        "order/finalize/discount/",
        FinalizeDiscount.as_view(),
        name="finalize_discoount",
    ),
]
