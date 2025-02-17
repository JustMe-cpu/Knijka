
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import book_list

urlpatterns = [
    path('', book_list, name='book_list'),  # Список книг на главной странице приложения
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)