from django.urls import path
from Сatering import settings
from . import views as main_menu_views
from django.conf.urls.static import static


urlpatterns = [
    path('', main_menu_views.main_menu, name='main'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)