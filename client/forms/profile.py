import re
from django import forms
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'phone_number', 'birth_date']

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        if not re.match(r'^09\d{9}$', phone):
            raise forms.ValidationError('شماره تلفن باید ۱۱ رقم و با ۰۹ شروع شود.')
        return phone
