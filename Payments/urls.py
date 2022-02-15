from django.urls import path
from . import views

app_name = 'Payments'

urlpatterns = [
    path('Process/', views.payment_process, name='Pay'),
    path('payment_successful/', views.payment_done, name='Done'),
    path('Cancel/', views.payment_canceled, name='Cancel'),
]
