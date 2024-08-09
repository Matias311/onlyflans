from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(req):
    """Muestra el index.html de templates"""
    context: dict = {
        "messege": "Bienvenido a Only Flans"
    }
    return render(req, 'index.html', context)


def about(req):
    """Nos muestra la informacion de sobre la pagina"""
    context: dict = {
        "messege": "Nuestra empresa ...."
    }
    return render(req, 'about.html', context)


def welcome(req):
    """Nos muestra la bienvenida a la tienda"""
    return render(req, 'welcome.html', {})
