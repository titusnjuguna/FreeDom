from django import forms
#added a comment
class CartAddForm(forms.Form):
    quantity = forms.IntegerField( required= True,
                         
                                    label= 'Qty',
                                    widget= forms.NumberInput(
                                        attrs= {'class' : 'form-control',
                                        'name': 'quantity',
                                        'value': '1',
                                        'min' : '1',
                                        'max' : '10',
                                        'step' : '1',
                                        'data-decimals': '0'


                                        }
                                    )

                                    )
   #override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
   
