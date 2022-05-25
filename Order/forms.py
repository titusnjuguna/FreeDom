from .models import Orders
from django import forms


class OrderCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['city'].widget.attrs.update({'class': 'form-control'})
        self.fields['postal_code'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['company'].widget.attrs.update({'class': 'form-control'})
        self.fields['order_note'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['apartment'].widget.attrs.update({'class': 'form-control'})
        self.fields['house'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control'})
        self.fields['state'].widget.attrs.update({'class': 'form-control'})
        self.fields['country'].widget.attrs.update({'class': 'form-control'})
    class Meta:
        model = Orders
        fields = ['first_name', 'last_name', 'email',
                  'city', 'postal_code', 'company', 'order_note', 
                  'apartment', 'house', 'phone', 'state', 'country',]


    
     
    
