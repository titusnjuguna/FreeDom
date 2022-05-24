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

        f_name = request.POST.get('F_name', default=None)
        l_name = request.POST.get('L_name','')
        company = request.POST.get('company', '')
        country = request.POST.get('country', '')
        house = request.POST.get('house','')
        suite = request.POST.get('suite','')
        city = request.POST.get('city','')
        state = request.POST.get('state','')
        Postcode = request.POST.get('Postcode','')
        Phone = request.POST.get('Phone','')
        email = request.POST.get('email','')
        order_note = request.POST.get('order_note','')

        order_form = OrderCreateForm(first_name=f_name, last_name=l_name, email=email,
                                city=city, postal_code=Postcode, company=company, order_note=order_note,
                                apartment=suite,house=house,phone=Phone, state=state,country=country)
        
        if order_form.is_valid():
            order = order_form.save()
                                    
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
    return render(request, 'Order/checkout.html',{'form':form,'cart':cart})
