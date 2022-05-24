from .models import Orders
from django import forms


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['first_name', 'last_name', 'email',
                  'city', 'postal_code', 'company', 'order_note', 
                  'apartment', 'house', 'phone', 'state', 'country',]


    
     
    
