from django import forms

PRODUCT_QUANTTITY_CHOICES=[(i,str(i)) for i in range(1,21)]

class CartAddForm(forms.Form):
    quantity = forms.TypedChoiceField(choices = PRODUCT_QUANTTITY_CHOICES, coerced = int)
    override = forms.BooleanField(
        required=False, initial=False, widget=forms.Hidden)
