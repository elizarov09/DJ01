# ZeroCoder/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')),  # Подключение URL-ов приложения news
    path('', include('main.urls')),  # Подключение URL-ов главного приложения
]
