from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
from ..forms import BuyerRegisterForm
from django.contrib.auth.models import User


class BuyerRegisterView(CreateView):
    model = User
    form_class = BuyerRegisterForm
    template_name = 'Users/Buyer/register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'buyer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('Buyer:login')
