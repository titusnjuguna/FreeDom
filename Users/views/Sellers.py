from django.shortcuts import render,redirect
from django.contrib.auth.models import User

from ..forms import SellerRegisterForm
from django.views.generic import CreateView
from django.contrib import login

# Create your views here.
class SellerRegisterView(CreateView):
    model = User
    form_class = SellerRegisterForm
    template_name = 'Users/Seller/register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'seller'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('Users:dashoard')
        
    


