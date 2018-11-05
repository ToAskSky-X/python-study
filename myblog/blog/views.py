from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return HttpResponse('Hello Django')


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) +int(b) 
    return HttpResponse(c)

def add2(request,a,b):
    return HttpResponse(a+b)
