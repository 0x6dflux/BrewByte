from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from client.models.user import User
from client.models import address, client_picture


# Register your models here.
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("phone_number","username","first_name","last_name")

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = "__all__"

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ("username", "phone_number", "first_name", "last_name", "user_code", "is_staff", "is_customer")
    search_fields = ("username", "phone_number","first_name", "last_name", "email", "user_code")
    fieldsets = (
        (None, {"fields": ("phone_number","username", "first_name", "last_name", "password")}),
        ("Personal info", {"fields": ("email","user_code", "birthday")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_customer"
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
        ("Other", {"fields": ()}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("phone_number","username", "first_name", "last_name",  "password1", "password2"),
            },
        ),
    )

admin.site.register(User,CustomUserAdmin)
# admin.site.register(customer_profile.CustomerProfile,manager_profile.ManagerProfile,)

# admin.site.register(address.Address,picture.Picture,)