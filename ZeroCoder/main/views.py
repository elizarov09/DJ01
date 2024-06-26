# main/views.py
from django.shortcuts import render
from django.http import HttpResponse
from news.models import News  # Импорт модели News из модуля news

# Ваши функции представления
def index(request):
    return render(request, 'main/index.html')

def new(request):
    return render(request, 'main/new.html')

def data(request):
    return HttpResponse("<h1>Это DJANGO DATA</h1>")

def test(request):
    return HttpResponse("<h1>Это DJANGO TEST</h1>")

def blog(request):
    return render(request, 'main/blog.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def about(request):
    return render(request, 'main/about.html')

def news(request):
    news = News.objects.all()
    return render(request, 'news/news.html', {'news': news})
