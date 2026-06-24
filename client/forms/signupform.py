import re
from django import forms
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="رمز عبور")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="تکرار رمز عبور")

    class Meta:
        model = CustomUser
        fields = [
            'phone_number',
            'username',
            'first_name',
            'last_name',
            'birthday',
        ]

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        if not re.match(r'^09\d{9}$', phone):
            raise forms.ValidationError('شماره تلفن باید ۱۱ رقم و با ۰۹ شروع شود.')
        if CustomUser.objects.filter(phone_number=phone).exists():
            raise forms.ValidationError('این شماره تلفن قبلاً ثبت شده است.')
        return phone

    def clean_birth_date(self):
        birth_date = self.cleaned_data.get('birthday')
        if not birth_date:
            raise forms.ValidationError('تاریخ تولد اجباری است.')
        return birth_date

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm = cleaned_data.get('confirm_password')
        if password and confirm and password != confirm:
            raise forms.ValidationError('رمز عبور و تکرار آن یکسان نیستند.')
        return cleaned_data
