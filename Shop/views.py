from contextlib import redirect_stdout
from django.shortcuts import get_object_or_404, redirect, render
from Cart.forms import CartAddForm
from .models import Category, Product


# Create your views here.
def product_list(request):
    products = Product.objects.filter(available=True)
    categories = Category.objects.all()
    latest_products = Product.objects.order_by('-created')[:7]
    return render(request,'Shop/Product/list.html',{'products':products,'categories':categories,'latest_products':latest_products})

def product_detail(request,id,slug):
    product = get_object_or_404(Product,slug=slug, id=id,available=True)
    cart_product_form = CartAddForm()
    return render(request,'Shop/Product/product.html', {'product': product,'cart_product_form':cart_product_form})

def product_category(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)
    return render(request, 'Shop/Product/category-list.html', {'categories': categories, 'products': products, 'category': category})

