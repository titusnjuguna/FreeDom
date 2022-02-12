from .models import Orders
from django import forms


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['first_name','last_name','email','address','city','postal_code']