from .models import Orders
from django import forms


class OrderCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget = forms.TextInput(attrs={'class':' col-sm-6 form-control','required':'true'})
        self.fields['last_name'].widget= forms.TextInput(attrs={'class':' col-sm-6 form-control','required':'true'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['city'].widget = forms.TextInput(
            attrs={'class': ' col-sm-6 form-control', 'required': 'true'})
        self.fields['postal_code'].widget = forms.TextInput(
            attrs={'class': ' col-sm-6 form-control', 'required': 'true'})
        self.fields['company'].widget.attrs.update({'class': 'form-control'})
        self.fields['order_note'].widget.attrs.update(
            {'class': 'form-control','cols':"30" ,'rows':"4",'placeholder':'Notes about your order'})
        self.fields['apartment'].widget.attrs.update({'class': 'form-control','placeholder':'Apartments, suite, unit'})
        self.fields['house'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'House number and Street name'})
        self.fields['phone'].widget = forms.TextInput(
            attrs={'class': ' col-sm-6 form-control', 'required': 'true'})
        self.fields['state'].widget = forms.TextInput(
            attrs={'class': ' col-sm-6 form-control', 'required': 'true'})
        self.fields['country'].widget.attrs={'class': 'form-control'}
        self.fields['payment_method'].widget.attrs={'class': 'form-control','type': 'CheckboxSelectMultiple'}
    class Meta:
        model = Orders
        fields = ['first_name', 'last_name', 'company', 'country','apartment', 'house',
                  'city', 'state', 'postal_code', 'phone', 'email',  'company', 'order_note',
                    'payment_method',]


    
     
    
