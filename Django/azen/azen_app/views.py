from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
  return HttpResponse(" Hello, Azen in Django ")


def JoseM(request):
  return HttpResponse(" Hello JoseM ")