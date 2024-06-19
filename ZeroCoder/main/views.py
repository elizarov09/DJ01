from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def new(request):
    return render(request, 'main/new.html')

def data(request):
    return HttpResponse("<h1>Это DJANGO DATA</h1>")

def test(request):
    return HttpResponse("<h1>Это DJANGO TEST</h1>")

def blog(request):
    return render(request, 'main/blog.html')  # Представление для страницы блога

def contacts(request):
    return render(request, 'main/contacts.html')  # Представление для страницы контактов

def about(request):
    return render(request, 'main/about.html')  # Представление для страницы о нас
