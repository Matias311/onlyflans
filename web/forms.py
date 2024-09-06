from django import forms
from .models import ContactForm, Profile, Flan
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ContactFormForm(forms.Form):
    customer_email = forms.EmailField(label='Correo')
    customer_name = forms.CharField(max_length=64, label='Nombre')
    message = forms.CharField(label='Mensaje')


class ProfileFrom(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'birth_date']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True, help_text='Requerido. Ingrese una direccion de correo electronico')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Este correo electronico ya esta en uso')
        return email


class AgregarFlan(forms.ModelForm):
    class Meta:
        model = Flan
        fields = ['name', 'description', 'image_url',
                  'slug', 'is_private', 'price']
        labels = {
            'name': 'Nombre',
            'description': 'Descripcion',
            'image_url': 'URL de la imagen',
            'slug': 'Apodo del producto',
            'is_private': 'Es solo para usuarios registrados',
            'price': 'Precio'
        }
