from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product, YarnCategory, ToolCategory, YarnBrand, ToolBrand, ProductCategory

# Create your views here.


def all_products(request):
    """
    A view to show all the products
    """
    products = Product.objects.all()
    query = None
    product_category = None
    yarn_category = None
    tool_category = None
    yarn_brand = None
    tool_brand = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            yarn_categories = None
            tool_categories = None
            sortkey = request.GET['sort']
            sort=sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
        
            if 'direction' in request.GET:
                yarn_categories = None
                tool_categories = None
                direction = request.GET['direction']
                if direction == 'asc':
                    sortkey = f'{sortkey}'
            products = products.order_by(sortkey)
        
        if 'product_category' in request.GET:
            sortkey = None
            tool_categories = None
            yarn_categories = None
            product_categories = request.GET['product_category'].split(',')
            products = products.filter(product_category__name__in=product_categories)
            product_categories = ProductCategory.objects.filter(name__in=product_categories)

        if 'yarn_category' in request.GET:
            sortkey = None
            tool_categories = None
            yarn_categories = request.GET['yarn_category'].split(',')
            products = products.filter(yarn_category__yarn_category_name__in=yarn_categories)
            yarn_categories = YarnCategory.objects.filter(yarn_category_name__in=yarn_categories)
        
        if 'yarn_brand' in request.GET:
            sortkey = None
            tool_categories = None
            yarn_categories= None
            tool_brands = None
            yarn_brands = request.GET['yarn_brand'].split(',')
            products = products.filter(yarn_brand__name__in=yarn_brands)
            yarn_brands = YarnBrand.objects.filter(name__in=yarn_brands)

        if 'tool_category' in request.GET:
            yarn_categories = None
            sortkey = None
            tool_categories = request.GET['tool_category'].split(',')
            products = products.filter(tool_category__tool_category_name__in=tool_categories)
            tool_categories = ToolCategory.objects.filter(tool_category_name__in=tool_categories)
        
        if 'tool_brand' in request.GET:
            sortkey = None
            tool_categories = None
            yarn_categories= None
            yarn_brands = None
            tool_brands = request.GET['tool_brand'].split(',')
            products = products.filter(tool_brand__name__in=tool_brands)
            tool_brands = ToolBrand.objects.filter(name__in=tool_brands)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didnt enter anything in the search bar!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
    
    
    current_sorting = f'{sort}_{direction}'

    return render(
        request,
        'products/products.html',
        {
            "products": products,
            "search_term": query,
            "yarn_categories": yarn_categories,
            "tool_categories": tool_categories,
            "current_sorting": current_sorting
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
