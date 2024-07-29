from django.urls import path
from Сatering import settings
from . import views as dishes_views
from django.conf.urls.static import static

app_name = 'dishes'

urlpatterns = [
    path('', dishes_views.CategoryCatalogListView.as_view(), name='category_catalog'),
    # path('/<slug:category_slug>/>', dishes_views.__!!!__.as_view(), name='category-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)