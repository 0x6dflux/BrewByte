from django import forms
from django.contrib.auth import get_user_model
from client.models import CustomerProfile
import re

CustomUser = get_user_model()


class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "phone_number", "birthday"]

    def clean_phone_number(self):
        phone = self.cleaned_data.get("phone_number")
        if not re.match(r"^09\d{9}$", phone):
            raise forms.ValidationError(
                "Phone Number Shall Contains 11 Characters, Starting With '09'!"
            )
        return phone

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'phone_number']

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        if phone and not re.match(r'^09\d{9}$', phone):
            raise forms.ValidationError("Phone Number Shall Contains 11 Characters, Starting With '09'!")
        return phone

class ProfileDetailsForm(forms.ModelForm):
    class Meta:
        model = CustomerProfile
        fields = ['profile_image']