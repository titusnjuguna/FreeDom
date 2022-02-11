from django.shortcuts import get_object_or_404, render
from Cart.forms import CartAddForm
from .models import Category, Product


# Create your views here.
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.objects.filter(category=category)
    return render(request,'Shop/Product/list.html',{'categories':categories,'products':products,'category':category})

def product_detail(request,id,slug):
    product = get_object_or_404(Product,slug=slug, id=id,available=True)
    cart_product_form = CartAddForm()
    return render(request,'Shop/Product/detail.html',{'product':product,'cart_product_form':cart_product_form})