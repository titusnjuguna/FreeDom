from celery import shared_task
from .models import Orders
from django.core.mail import send_mail

@shared_task
def order_created(order_id):
    order = Orders.objects.get(id=order_id)

    subject = f'Order {order_id} has been received'
    message = f'Dear {order.first_name},\n\n' \
    f'You have successfully placed an order.' \
    f'Your order ID is {order.id}. The order is ready for shipping. We will work hard to ensure the order is delivered on time'
    mail_sent = send_mail(subject,
    message,'FreeDom Mall',[order.email])
    return mail_sent