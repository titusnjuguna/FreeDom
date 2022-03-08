from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Cart/', include('Cart.urls', namespace='Cart')),
    path('orders/', include('Order.urls', namespace='Order')),
    path('Pay/', include('Payments.urls', namespace='Payments')),
    path('Api/', include('Shop.api.urls',namespace='Api')),
    path('User/', include('Users.urls', namespace='Users')),
    path('', include('Shop.urls', namespace='Shop')),
]
