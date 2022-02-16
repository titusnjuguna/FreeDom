from wsgiref.util import application_uri
from django.urls import path
from . import views 

app_name = 'Shop'

urlpatterns = [
    path('shop/', views.ProductListView.as_view(),name='Product_list'),
    path('shop/<pk>/',views.ProductDetailView.as_view(),name='Product_detail'),
    ]