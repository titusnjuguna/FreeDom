from decimal import Decimal
from django.conf import settings
from Shop.models import Product

# creating cart and methods to update the cart
class Cart(object):
    #intializing cart
    def __init__(self,request):
        # requesting user session
        
        self.session = request.session
        # retrieve the content of the cart
        cart = self.session.get(settings.CART_SESSION_ID)
        
        if not cart:
            #if no cart is present in the session create an empty cart
            cart = self.session[settings.CART_SESSION_ID]={}
        self.cart = cart
    # method to add products into the cart
    def add(self,product, quantity=1,override_quantity= False):

        product_id = str(product.id)
        # check if product is in the cart
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity':0,'price':str(product.price)}
        if override_quantity:
            self.cart[product_id]['quantity']= quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self,product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
        self.save()

    def __iter__(self):

        product_id = self.cart.keys()
        products = Product.objects.filter(id__in= product_id)
        cart = self.cart

        for product in products:
            cart[str('product_id')][product]= product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item
        
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price'])* item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.cart.session[settings.CART_SESSION_ID]
        self.save()
