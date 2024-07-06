from django.shortcuts import render


# Create your views here.
def main_menu(request):
    data = {
        'title': 'Главная страница',
    }
    return render(
        request,
        'main_menu/home.html',
        data

    )
