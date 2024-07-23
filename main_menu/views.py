from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class IndexView(TemplateView):
    template_name = 'main_menu/index.html'
    extra_context = {
        'title': 'Главная страница',
    }

class AboutView(TemplateView):
    template_name = 'main_menu/about.html'
    extra_context = {
        'title': 'О нас',
    }