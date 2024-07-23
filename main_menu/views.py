from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class IndexView(TemplateView):
    template_name = 'main_menu/index.html'
    extra_context = {
        'title': 'Главная страница',
    }

def about(request):
    data = {
        'title': 'О нас',
    }
    return render(
        request,
        'main_menu/about.html',
        context=data,
    )