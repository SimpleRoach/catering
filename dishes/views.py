from django.shortcuts import render
from django.views.generic import ListView

from .models import Categories
from .utils import DataMixin


# Create your views here.
class CategoryCatalogListView(DataMixin, ListView):
    model = Categories
    template_name = 'dishes/category_catalog.html'
    context_object_name = 'categories'
    title_page = 'Каталог'

    def get_context_data(self, **kwargs):
        # Получаем базовый контекст от ListView
        context = super().get_context_data(**kwargs)
        # Добавляем контекст из DataMixin
        context = DataMixin.get_context_data(self, **context)
        return context