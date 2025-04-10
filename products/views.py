from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.db.models import Q
from .models import Product, YarnCategory, ToolCategory, YarnBrand, ToolBrand, ProductCategory
from checkout.models import Order
from .forms import ProductForm, AdminOrder

# Create your views here.


def all_products(request):
    """
    A view to show all the products
    Some code taken from the Boutique Ado walkthrough project
    """
    products = Product.objects.all()
    yarn_categories = YarnCategory.objects.all()
    query = None
    product_category = None
    sort = None
    direction = None
    categories = None
    category = None
    brands = None
    brand = None
    
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort=sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
        
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'asc':
                    sortkey = f'{sortkey}'
            products = products.order_by(sortkey)
        
        if 'product_category' in request.GET:
            sortkey = None
            product_categories = request.GET['product_category'].split(',')
            products = products.filter(product_category__name__in=product_categories)
            product_categories = ProductCategory.objects.filter(name__in=product_categories)
        
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            if request.GET['category'] in ['4_ply', 'aran', 'dk']:
                products = products.filter(yarn_category__yarn_category_name__in=categories)
                categories == YarnCategory.objects.filter(yarn_category_name__in=categories)

            elif request.GET['category'] in ['crochet_hooks_and_needles', 'counters_and_markers', 'yarn_bowls', 'other']:
                products = products.filter(tool_category__tool_category_name__in=categories)
                categories = ToolCategory.objects.filter(tool_category_name__in=categories)
        
        if 'brand' in request.GET:
            brands = request.GET['brand'].split(',')
            if request.GET['brand'] in ['creative_cotton', 'crochet_society', 'scheepjes_chunky_monkey', 'west_yorkshire_spinners_signature']:
                products = products.filter(yarn_brand__name__in=brands)
                brands == YarnBrand.objects.filter(name__in=brands)

            elif request.GET['brand'] in ['bella_coco','clover_armour','crochet_society','knit_pro', 'pony', 'sirdar']:
                products = products.filter(tool_brand__name__in=brands)
                categories = ToolBrand.objects.filter(name__in=brands)

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
            "product_category": product_category,
            "current_brands": brands,
            "current_sorting": current_sorting,
            "current_categories": categories,
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





@login_required
def add_product(request):
    """
    Add a product to the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admins can create, update or delete products')
        return redirect(reverse('home'))
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'You have successfully added the product')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please check that the form is valid and try again')
    else:
        form = ProductForm()
    
    return render(
        request,
        'products/add_product.html',
        {
            "form": form,
        }
    )


@login_required
def edit_product(request, product_id):
    """
    Edit a product in the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admins can create, update or delete products')
        return redirect(reverse('home'))
    
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully updated product')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product! Please check that the form is valid')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    return render(
        request,
        'products/edit_product.html',
        {
            'form': form,
            'product': product,
        }
    )


@login_required
def delete_product(request, product_id):
    """
    Delete a product in the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admins can create, update or delete products')
        return redirect(reverse('home'))
    
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product has been deleted!')
    return redirect(reverse('products'))




