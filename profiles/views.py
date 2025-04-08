from django.shortcuts import render, get_object_or_404

from .models import UserProfile
from .forms import UserProfileForm


def profile(request):
    """ Display the user's profile. """

    profile = get_object_or_404(UserProfile, user=request.user)
    form = UserProfileForm(instance=profile)

    return render(
        request,
        'profiles/profile.html',
        {
            "form": form,
        }
    )


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
