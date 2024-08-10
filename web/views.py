from django.shortcuts import render
from django.http import HttpResponse
from .models import Flan

# Create your views here.


def home(req):
    """Muestra el index.html de templates"""
    context: dict = {
        'flanes_publicos': Flan.objects.filter(is_private=False),
        'usuario': {"nombre": "Matias", "is_active": True}
    }
    return render(req, 'index.html', context)


def about(req):
    """Nos muestra la informacion de sobre la pagina"""
    context: dict = {
        "messege": "Nuestra empresa ....",
        'usuario': {"nombre": "Matias", "is_active": True}
    }
    return render(req, 'about.html', context)


def welcome(req):
    """Nos muestra la bienvenida a la tienda"""
    context: dict = {
        'usuario': {"nombre": "Matias", "is_active": True},
        'flanes_publicos': Flan.objects.filter(is_private=False),
        'flanes_privados': Flan.objects.filter(is_private=True)
    }
    return render(req, 'welcome.html', context)
