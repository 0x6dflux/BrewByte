from django.http import HttpResponse
from django.urls import path, include
from general.views import HomeView

app_name = 'general'
urlpatterns = [
    path("", HomeView.as_view(), name="home" ),

]