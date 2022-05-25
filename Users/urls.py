from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'Users'

urlpatterns = [
    path('register/', views.register, name='Register'),
    path('login/', auth_views.LoginView.as_view(template_name='Users/login.html'), name='Login'),
    
]