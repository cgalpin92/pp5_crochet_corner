from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There is nothing in your basket at the moment")
        return redirect(reverse('products'))
    
    order_form = OrderForm()

    return render(
        request,
        'checkout/checkout.html',
        {
            "order_form": order_form
        }
    )