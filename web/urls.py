# Pagina donde se ponen los endpoint de la web
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('about', views.about),
    path('welcome', views.welcome),
    path('contacto', views.contacto),
    path('exito', views.exito),
    path('detalle/<uuid:flan_uuid>', views.detalle_flan, name='detail_flan'),
    path('detalle_privados/<uuid:flan_uuid>',
         views.detalle_flan_privado, name='detalle_privado'),
    path('profile/', views.profile_view, name='profile'),
    path('register/', views.register)
]
