from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def hola(req):
    """Muestra el index.html de templates"""
    return render(req, 'index.html')
