from .models import buyer,Seller
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import transaction

class SellerRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'
        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_seller = True
        user.save()
        Seller.objects.create(user=user)
        return user


class BuyerRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=User
       

    def save(self):
        user = super().save(commit=False)
        user.is_buyer = True
        if commit:
            user.save()
        return user








