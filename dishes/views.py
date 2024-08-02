# from django.shortcuts import render
from django.views.generic import ListView

from .models import Categories, Products
from .utils import DataMixin

# Create your views here.
class CategoryCatalogListView(DataMixin, ListView):
    model = Categories
    template_name = 'dishes/category_catalog.html'
    context_object_name = 'categories'
    title_page = 'Каталог'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=self.title_page)


class DishesByCategoryCatalogListView(DataMixin, ListView):
    slug_url_kwarg = 'dishes_catrgory_slug'
    model = Products
    tamplate_name = 'dishes_category_catalog.html'
    context_object_name = 'dishes'
    title_page = ''
