from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from checkout.models import Order
from .forms import UserProfileForm


@login_required
def profile(request):
    """ Display the user's profile. """

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'Your account has been updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    return render(
        request,
        'profiles/profile.html',
        {
            "form": form,
            'on_profile_page': True
        }
    )


@login_required
def order_history(request):
    """
    Displays the users order history
    """

    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()

    return render(
        request,
        'profiles/order_history.html',
        {
            "orders": orders
        }
    )


@login_required
def order_history_item(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    order_date = get_object_or_404(Order, date=order.date)

    messages.info(request, (
        f'Order confirmation for order number {order_number}.'
        'A confirmation email was sent to you on {order_date}'
    ))
    
    return render(
        request,
        'checkout/checkout_success.html',
        {
            "order": order,
            "order_date": order_date,
            "from_order_history": True,
        }
    )