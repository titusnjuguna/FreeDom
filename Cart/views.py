from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from Shop.models import Product
from .cart import Cart
from .forms import CartAddForm

# Create your views here.
@require_POST
def CartAdd(request,product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id= product_id)
    form = CartAddForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity= cd['quantity'],  override_quantity = cd['override'])
    return redirect('Cart:cart_detail')

@require_POST
def CartRemove(request,product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('Cart:cart_detail')

def Cart_detail(request):
    cart = Cart(request)
    return render(request,'Cart/detail.html',{'cart':cart})