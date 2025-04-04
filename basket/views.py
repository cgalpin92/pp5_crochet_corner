from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.


def view_basket(request):
    """
    A view to returns the basket contents page
    Taken from the Boutique Ado walkthrough project
    """
    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """
    Adds products to the shopping basket
    Taken from the Boutique Ado walkthrough project
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        messages.success(request, f'You updated the quantity of {product.name} to {basket[item_id]}')
    else:
        basket[item_id] = quantity
        messages.success(request, f'Added {product.name} to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """
    Adjusts the quantity of the specified product 
    Taken from the Boutique Ado walkthrough project
    """

    product = get_object_or_404(Product, pk=item_id)

    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
        messages.success(request, f'You updated {product.name} quantity to {basket[item_id]}')
    else:
        basket.pop(item_id)
        messages.success(request, f'You removed {product.name} from your basket')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """
    Remove the item from the shopping basket 
    Taken from the Boutique Ado walkthrough project
    """
    
    
    try:
        product = get_object_or_404(Product, pk=item_id)
        basket = request.session.get('basket', {})

        basket.pop(item_id)
        messages.success(request, f'You removed {product.name} from your basket')

        request.session['basket'] = basket
        return HttpResponse(status=200)
    
    except Exception as e:
        messages.error(request, f'Error removing the item from your basket: {e}')
        return HttpResponse(status=500)
    
