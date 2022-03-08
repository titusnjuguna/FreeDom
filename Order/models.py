from django.db import models
from Shop.models import Product,Store
from Users.models import buyer
# Create your models here.
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
    store = models.ForeignKey(Store,on_delete= models.CASCADE , related_name='store_order')
    customer = models.ForeignKey(buyer, on_delete= models.CASCADE)

    class Meta:
        ordering = ['-created',]

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