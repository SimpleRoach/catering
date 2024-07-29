# from django.shortcuts import render
from django.views.generic import ListView

from .models import Categories
from .utils import DataMixin


# Create your views here.
class CategoryCatalogListView(DataMixin, ListView):
    model = Categories
    template_name = 'dishes/category_catalog.html'
    context_object_name = 'categories'
    title_page = 'Каталог'
    # slug_url_kwarg = 'post_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=self.title_page)

