from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    APIListView,
    CreateApiView,
    DetailAPIView,
    UpdateAPIView,
    DeleteAPIView
)

from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('api/list', APIListView.as_view(), name = 'api-list'),
    path('api/list/<int:id>', DetailAPIView.as_view(), name = 'list-detials'),
    path('api/create/', CreateApiView.as_view(), name = 'create'),
    path('api/update/<int:id>', UpdateAPIView.as_view(), name = 'update-api'),
    path('api/delete/<int:id>', DeleteAPIView.as_view(), name = 'delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

