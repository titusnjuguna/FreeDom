from django.db import models
from Shop.models import Product

# Create your models here.
PAYMENT_OPTIONS =(
    ('mpesa','MPESA'),
    ('direct bank transfer', 'BANK2BANK'),
    ('cash on delivery','CASH ON DELIVERY'),
    ('paypal','PAYPAL'),
    ('credit card','CREDIT CARD')


)
class Orders(models.Model):

    braintree_id = models.CharField(max_length=150, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=50)
    city = models.CharField(max_length=100, blank=False)
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    state = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=15 , blank=True, null=True)
    house = models.CharField(max_length=100, blank=True, null=True)
    apartment = models.CharField(max_length=100, blank=True, null=True)
    order_note = models.TextField(max_length=200,blank=True,null=True)
    company = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=30,blank=True, null=True)
    payment_method = models.CharField(max_length=30, choices= PAYMENT_OPTIONS,default='mpesa')

    class Meta:
        ordering = ['-created',]
        verbose_name = 'Order'

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        #review  this line later
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Orders,on_delete= models.CASCADE ,related_name='items')
    product = models.ForeignKey(Product,on_delete= models.CASCADE, related_name='order_item')
    price = models.DecimalField(max_digits=10, decimal_places= 2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price*self.quantity
