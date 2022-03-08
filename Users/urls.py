from django.urls import path
from django.contrib.auth import views as auth_views
from .views import Buyers,Sellers


app_name = 'Users'

urlpatterns = [
    path('Users/Buyer/register/', Buyers.BuyerRegisterView, name='Buyer_Register'),
    path('Users/Seller/register/', Sellers.SellerRegisterView, name='Seller_Register'),
    path('login/', auth_views.LoginView.as_view(template_name='Users/login.html'), name='Login'),
    
]