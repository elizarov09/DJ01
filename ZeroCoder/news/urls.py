from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name='news'),  # Основной маршрут для news
    path('new/', views.new, name='new'),
    path('data/', views.data, name='data'),
    path('test/', views.test, name='test'),
    path('blog/', views.blog, name='blog'),
    path('contacts/', views.contacts, name='contacts'),
    path('about/', views.about, name='about'),
]
