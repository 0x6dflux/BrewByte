from django import forms
from django.conf import settings

User = settings.AUTH_USER_MODEL


class SignInForm(forms.Form):
    phone_number = forms.CharField(max_length=15, label="Phone Number")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
