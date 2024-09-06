from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from .models import Flan, ContactForm, Profile
from .forms import ContactFormForm, UserForm, ProfileFrom, CustomUserCreationForm, AgregarFlan
from django.contrib.auth import login
# Create your views here.


def home(req):
    """Muestra el index.html de templates"""
    context: dict = {
        'flanes_publicos': Flan.objects.filter(is_private=False),
    }
    return render(req, 'index.html', context)


def about(req):
    """Nos muestra la informacion de sobre la pagina"""
    context: dict = {
        "messege": "Nuestra empresa ....",
    }
    return render(req, 'about.html', context)


@login_required
def welcome(req):
    """Nos muestra la bienvenida a la tienda"""
    context: dict = {
        'flanes_publicos': Flan.objects.filter(is_private=False),
        'flanes_privados': Flan.objects.filter(is_private=True),
        'usuario': req.user.id
    }
    return render(req, 'welcome.html', context)


def exito(req):
    context = {}
    return render(req, 'exito.html', context)


def contacto(req):
    if req.method == 'POST':
        form = ContactFormForm(req.POST)
        if form.is_valid():
            ContactForm.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/exito')
    else:
        form = ContactFormForm()

    context = {
        'form': form
    }
    return render(req, 'contacto.html', context)


def detalle_flan(req, flan_uuid):
    flan = Flan.objects.get(flan_uuid=flan_uuid)
    if flan.is_private == False:
        return render(req, 'description-flan.html', {"flan": flan})


@login_required
def detalle_flan_privado(req, flan_uuid):
    flan = Flan.objects.get(flan_uuid=flan_uuid)
    return render(req, 'description-flan.html', {"flan": flan})


@login_required
def profile_view(req):
    user_id = req.user.id

    user = req.user
    if not hasattr(user, 'profile'):
        Profile.objects.create(user=user)
        profile = Profile.objects.get(user_id=user_id)
        print(f'user profile get -> {profile.__dict__}')

    if req.method == 'POST':
        user_form = UserForm(req.POST, instance=req.user)
        profile_form = ProfileFrom(req.POST, instance=req.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('/welcome')
    else:
        user_form = UserForm(instance=req.user)
        profile_form = ProfileFrom(instance=req.user.profile)
    return render(req, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


def register(req):
    if req.method == 'POST':
        form = CustomUserCreationForm(req.POST)
        if form.is_valid():
            user = form.save()
            login(req, user)
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(req, 'register.html', {'form': form})


@login_required
def agregar_flan(req):
    if not req.user.is_superuser:
        return HttpResponseForbidden("No tienes permisos para acceder a esta pagina")

    if req.method == 'POST':
        form = AgregarFlan(req.POST)
        if form.is_valid():
            form.save()
            return redirect('welcome')
    else:
        form = AgregarFlan()

    return render(req, 'agregar_flan.html', {'form': form})
