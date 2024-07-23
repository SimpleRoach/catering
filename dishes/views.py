from django.shortcuts import render
from django.views.generic import ListView

from .models import Categories


# Create your views here.
class CatalogListView(ListView):
    model = Categories
    template_name = 'dishes/catalog.html'
    context_object_name = 'categories'
    categories = Categories.objects.all()
    extra_context = {
        'title' : 'Каталог',
        'categories': categories
    }

def product(request):
    data = {
        'title': 'О товаре',
    }
    return render(
        request,
        'dishes/product.html',
        context=data,
    )