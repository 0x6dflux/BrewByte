# client/urls.py

from django.urls import path
from .views import SignUpView, SignInView, sign_out_view, profile_edit_view

app_name = "client"

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("signin/", SignInView.as_view(), name="signin"),
    path("signout/", sign_out_view, name="signout"),
    path("profile/edit/", profile_edit_view, name="profile_edit"),
]
