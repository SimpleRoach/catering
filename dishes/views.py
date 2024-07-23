from django.shortcuts import render
from django.views.generic import ListView

from .models import Categories
from .utils import DataMixin


# Create your views here.
class CatalogListView(DataMixin, ListView):
    model = Categories
    template_name = 'dishes/catalog.html'
    context_object_name = 'categories'
    title_page = 'Каталог'