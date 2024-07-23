from django.shortcuts import render
from django.views.generic import TemplateView

from .utils import DataMixin
# Create your views here.

class IndexView(DataMixin, TemplateView):
    template_name = 'main_menu/index.html'
    title_page = 'Главная страница'


class AboutView(DataMixin, TemplateView):
    template_name = 'main_menu/about.html'
    title_page = 'О нас'