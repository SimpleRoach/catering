from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_menu.urls', namespace='main_menu')),
    path('catalog/', include('dishes.urls', namespace='dishes')),
]
