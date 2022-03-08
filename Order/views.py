from Cart.cart import Cart
from .models import OrderItem
from django.urls import reverse
from .tasks import order_created
from .forms import OrderCreateForm
from django.shortcuts import render,redirect
# Create your views here.

def Order_Create(request):
    cart = Cart(request)
    if request.method =='POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit= False)
            for item in cart:
                OrderItem.objects.create(order=order,product=item['product'],
                price=item['price'], quantity=item['quantity'])
            cart.clear()
            #launch async task, thwe daly method is called to execute the task async
            order_created.delay(order.id) 
            request.session['order_id'] = order.id
            return redirect(reverse('Payments:Pay'), {'order': order})
    else:
        form = OrderCreateForm()
        return render(request, 'Order/create.html',{'form':form,'cart':cart})
