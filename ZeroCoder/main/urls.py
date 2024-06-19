from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('data/', views.data, name='data'),
    path('test/', views.test, name='test'),
    path('blog/', views.blog, name='blog'),  # Добавляем маршрут для страницы блога
    path('contacts/', views.contacts, name='contacts'),  # Добавляем маршрут для страницы контактов
    path('about/', views.about, name='about'),  # Добавляем маршрут для страницы о нас
]
