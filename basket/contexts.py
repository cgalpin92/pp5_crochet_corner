from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def basket_contents(request):
    """
    Taken from the Boutique Ado walkthrough project
    """
    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})

    for item_id, quatity in basket.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quatity * product.price
        product_count += quatity
        basket_items.append({
            'item_id': item_id,
            'quantity': quatity,
            'product': product,
        })

    if total < settings.FREE_DELIVERY_LIMIT:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_LIMIT - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_limit': settings.FREE_DELIVERY_LIMIT,
        'grand_total': grand_total
    }

    return context
