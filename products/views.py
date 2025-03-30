from django.shortcuts import render, get_object_or_404
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


def product_details(request, product_id):
    """
    A view to show individual product information
    """

    product = get_object_or_404(Product, pk=product_id)

    return render(
        request,
        'products/product_details.html',
        {
            "product": product
        }
    )
