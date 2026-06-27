from django.urls import path
from general.views import HomeView

app_name = "general"
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
]
