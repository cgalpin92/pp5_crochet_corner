from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product, YarnCategory

# Create your views here.


def all_products(request):
    """
    A view to show all the products
    """
    products = Product.objects.all()
    query = None
    yarn_category = None

    if request.GET:
        if 'yarn_category' in request.GET:
            yarn_categories = request.GET['yarn_category'].split(',')
            products = products.filter(yarn_category__yarn_category_name__in=yarn_categories)
            yarn_categories = YarnCategory.objects.filter(yarn_category_name__in=yarn_categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didnt enter anything in the search bar!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    return render(
        request,
        'products/products.html',
        {
            "products": products,
            "search_term": query,
            "yarn_categories": yarn_categories
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
