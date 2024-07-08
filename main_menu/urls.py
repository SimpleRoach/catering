from django.urls import path
from Сatering import settings
from . import views as main_menu_views
from django.conf.urls.static import static


urlpatterns = [
    path('', main_menu_views.index, name='index'),
    path('about/', main_menu_views.about, name='about'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)