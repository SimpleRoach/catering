from django.shortcuts import render
from .models import Categories


# Create your views here.
def catalog(request):
    categories = Categories.objects.all()
    data = {
        'title' : 'Каталог',
        'categories' : categories
    }
    return render(
        request,
        'dishes/catalog.html',
        context=data,
    )

def product(request):
    data = {
        'title': 'О товаре',
    }
    return render(
        request,
        'dishes/product.html',
        context=data,
    )