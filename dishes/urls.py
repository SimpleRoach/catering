from django.urls import path
from Сatering import settings
from . import views as dishes_views
from django.conf.urls.static import static

app_name = 'dishes'

urlpatterns = [
    path('', dishes_views.CatalogListView.as_view(), name='catalog'),
    path('product/', dishes_views.product, name='product'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)