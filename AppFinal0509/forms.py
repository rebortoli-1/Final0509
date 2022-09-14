from asyncio.windows_events import NULL
from email.policy import default
from multiprocessing import Value
from tkinter.tix import Form
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class ProyectoFormulario(forms.Form):

    nombre= forms.CharField(max_length=40)
    jefatura=forms.CharField(max_length=40)
    gerencia=forms.CharField(max_length=40)
    devops=forms.NullBooleanField()

class MetricaFormulario(forms.Form):

    nombre= forms.CharField(max_length=40)
    proyecto=forms.CharField(max_length=40)
    observacion=forms.CharField(max_length=90)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

# Clase 24, agregamos el UserEditForm
class UserEditForm(UserCreationForm):

    # Obligatorios
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repetir la contraseña', widget=forms.PasswordInput)

    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'last_name', 'first_name']