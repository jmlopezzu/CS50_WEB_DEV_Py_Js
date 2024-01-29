from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def index(request):
#   return HttpResponse(" Hello, Azen in Django ! ")

def index(request):
  return render(request, "azen_app/index.html")
  
def JoseM(request):
  return HttpResponse(" Hello JoseM ")

def azen(request):
  return HttpResponse(" Hello azen ")

# def greet(request, name):
#     return HttpResponse(f"Hello, bienvenido ... {name.capitalize()}")

def greet(request, name):
    return render(request, "azen_app/greet.html",{
      "name": name.capitalize()
    })




