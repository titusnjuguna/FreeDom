from statistics import quantiles
from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from Cart.cart import Cart
from .tasks import order_created

# Create your views here.

def Order_Create(request):
    cart = Cart(request)
    if request.method =='POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,product=item['product'],
                price=item['price'], quantity=item['quantity'])
            cart.clear()
            #launch async task, thwe daly method is called to execute the task async
            order_created.delay(order.id) 
            return render(request, 'Order/order_created.html',{'order':order})
    else:
        form = OrderCreateForm()
        return render(request, 'Order/create.html',{'form':form,'cart':cart})
