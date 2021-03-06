from Cart.cart import Cart
from .models import OrderItem
from django.urls import reverse
from .tasks import order_created
from .forms import OrderCreateForm
from django.shortcuts import render,redirect
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.

def Order_Create(request):
    cart = Cart(request)
    if request.method =='POST':
        form =  OrderCreateForm(request.POST)
        if form.is_valid():
            payment = form.cleaned_data['payment_method']
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,product=item['product'],
                price=item['price'], quantity=item['quantity'])
            cart.clear()
            #launch async task, thwe daly method is called to execute the task async
            order_created.delay(order.id) 
            request.session['order_id'] = order.id
            if payment == 'MPESA':
                return redirect(reverse('Payments:Pay'))
            elif payment == 'BANK2BANK':
                return redirect(reverse('Payments:Pay'))
            elif payment == 'PAYPAL':
                return redirect(reverse('Payments:Pay'))
            elif payment == 'CASH ON DELIVERY':
                return redirect(reverse('Payments:Pay'))
            else:
                return redirect(reverse('Payments:Pay'))
    else:
        form = OrderCreateForm()
    return render(request, 'Order/checkout.html',{'form':form,'cart':cart})
