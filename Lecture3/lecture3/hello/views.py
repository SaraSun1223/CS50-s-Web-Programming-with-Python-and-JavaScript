from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello World!")

def sara(request):
    return HttpResponse("Hello, Sara!")
