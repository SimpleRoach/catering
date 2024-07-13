from django.contrib import admin
from django.urls import path, include

from Сatering import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_menu.urls', namespace='main_menu')),
    path('catalog/', include('dishes.urls', namespace='dishes')),
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]