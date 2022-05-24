from ast import Or

import braintree
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from Order.models import Orders

# instantiate Braintree payment gateway
gateway = braintree.BraintreeGateway(settings.BRAINTREE_CONF)


def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Orders, id=order_id)
    total_cost = order.get_total_cost()

    if request.method == 'POST':
        # get to nonce
        nonce = request.POST.get('payment_method_nonce', None)
        # create and post transactions
        results = gateway.transaction.sale({
            'amount': f'{total_cost:.2f}',
            'payment_method_nonce': nonce,
            'options': {
                'submit_for_settlement': True
            }
        })
        if results.is_success:
            # mark the order as paid
            order.paid = True
            # store transaction id 
            order.braintree_id = results.transaction.id
            order.save()
            return redirect('Payments:Done')
        else:
            return redirect('Payments:Cancel')
    else:
        client_token = gateway.client_token.generate()

        return render(request,'Payments/pay.html',
        {'order': order,'client_token': client_token})



def payment_done(request):
    return render(request, 'Payments/pay_done.html')

def payment_canceled(request):
    return render(request, 'Payments/cancel_pay.html')