from django.contrib import admin
from .models import OrderItem,Orders
# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display= ['first_name','last_name','email','address','postal_code','city','created',
                   'updated', 'paid', 'payment_method']
    list_filter= ['paid','created','updated','payment_method',]
    inlines = [OrderItemInline]

