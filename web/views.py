from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.


def cargar_json():
    with open('web/utils/flans.json', 'r') as file:
        data = json.load(file)
    return data


def home(req):
    """Muestra el index.html de templates"""
    context: dict = {
        'produtos': cargar_json(),
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
        'usuario': {"nombre": "Matias", "is_active": True}
    }
    return render(req, 'welcome.html', context)
