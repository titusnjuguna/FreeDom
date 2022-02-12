from django.urls import path
from . import views

app_name = 'Order'

urlpatterns = [
    path ('create/', views.Order_Create, name='Create_order'),

]
    


    
        
