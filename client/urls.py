from django.urls import path
from .views.profile import ProfileEditView
from .views.address import address_add_view, address_edit_view, address_delete_view
from .views.signin import SignInView
from .views.signup import SignUpView
from .views.signout import sign_out_view

app_name = "client"

urlpatterns = [
    path("signin/", SignInView.as_view(), name="signin"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("signout/", sign_out_view, name="signout"),
    path("profile/edit/", ProfileEditView.as_view(), name="profile_edit"),
    path("address/add/", address_add_view, name="address_add"),
    path("address/edit/<int:id>/", address_edit_view, name="address_edit"),
    path("address/delete/<int:id>/", address_delete_view, name="address_delete"),
]