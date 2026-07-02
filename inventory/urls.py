from django.urls import path

from inventory.views import ProductView

app_name = "inventory"

urlpatterns = [
    path("product/<int:id>/", ProductView.as_view(), name="product"),
]
