from django import forms
from client.models import Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['name', 'postal_address']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})