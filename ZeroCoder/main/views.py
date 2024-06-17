from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello DJANGO</h1>")

def new(request):
    return HttpResponse("<h1>Hello DJANGO - 2</h1>")

def data(request):
    return HttpResponse("<h1>Это DJANGO DATA</h1>")

def test(request):
    return HttpResponse("<h1>Это DJANGO TEST</h1>")