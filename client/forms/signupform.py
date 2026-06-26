import re
from django import forms
from django.conf import settings

CustomUser = settings.AUTH_USER_MODEL


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    confirm_password = forms.CharField(
        widget=forms.PasswordInput, label="Confirm Password"
    )

    class Meta:
        model = CustomUser
        fields = [
            "phone_number",
            "username",
            "first_name",
            "last_name",
            "birthday",
        ]

    def clean_phone_number(self):
        phone = self.cleaned_data.get("phone_number")
        if not re.match(r"^09\d{9}$", phone):
            raise forms.ValidationError(
                "Phone Number Shall Contains 11 Characters, Starting With '09'!"
            )
        if CustomUser.objects.filter(phone_number=phone).exists():
            raise forms.ValidationError("This Phone Number Has Been Registered Before!")
        return phone

    def clean_birth_date(self):
        birth_date = self.cleaned_data.get("birthday")
        if not birth_date:
            raise forms.ValidationError("Birthdate Is Required!")
        return birth_date

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm = cleaned_data.get("confirm_password")
        if password and confirm and password != confirm:
            raise forms.ValidationError("Password Is Not Confirmed!")
        return cleaned_data
