# Pagina donde se ponen los endpoint de la web
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('about', views.about),
    path('welcome', views.welcome)
]
