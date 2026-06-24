from django.http import HttpResponse
from django.urls import path, include
from general.views import HomeView
from general.views import add_to_cart
app_name = 'general'
urlpatterns = [
    path("", HomeView.as_view(), name="home" ),
    path("cart/update/", add_to_cart),

]