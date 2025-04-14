from django.shortcuts import render

# Create your views here.


def index(request):
    """
    A view to return the index page
    """
    return render(
        request,
        'home/index.html'
    )


def newsletter(request):
    """
    A view to display the newlsetter signup form
    """
    return render(
        request,
        'home/newsletter.html'
    )
