from django.urls import path

from sale.views import CreateOrder


app_name = "sale"

urlpatterns = [
    path("order/new/", CreateOrder.as_view(), name="create_order"),

]