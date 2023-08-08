from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def index(request):
#     return HttpResponse("Hello World!")

# Add index.html in templates/hello
def index(request):
    return render(request, "hello/index.html")

def sara(request):
    return HttpResponse("Hello, Sara!")

# 
# def greet(request,name):
#     return HttpResponse(f"Hello, {name.capitalize()}!")

# Add greet.html in templates/hello
def greet(request,name):
    return render(request,"hello/greet.html",{
        "name": name.capitalize()
    })
