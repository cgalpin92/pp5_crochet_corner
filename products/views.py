from django.shortcuts import render
from .models import Product

# Create your views here.

def all_products(request):
    """
    A view to show all the products
    """
    products_all = Product.objects.all()

    return render(
        request,
        'products/products.html',
        {
            "products_all": products_all,
        }
    )