from django.shortcuts import render



# Create your views here.
def catalog(request):
    data = {
        'title': 'Каталог',
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