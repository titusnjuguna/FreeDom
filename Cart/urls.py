from django.urls import path
from . import views

app_name='Cart'

urlpatterns = [
    path('', views.Cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.CartAdd, name='Cart_Add'),
    path('remove/<int:product_id>/', views.CartRemove, name='Cart_Remove'),
]