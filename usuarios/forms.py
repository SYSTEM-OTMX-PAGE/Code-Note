from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario


class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)
    foto_perfil = forms.ImageField(required=False)

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2', 'foto_perfil']