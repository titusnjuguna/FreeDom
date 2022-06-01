from django import template
from ..models import Product

register = template.Library()

@register.inclusion_tag("Shop/Product/list.html")
def new_arrivals(count=4):
    new_arrivals = Product.objects.order_by('-created')[:count]
    return {'new_arrivals': new_arrivals}

