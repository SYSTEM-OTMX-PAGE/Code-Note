from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.shortcuts import render

def login(request):
    data = {
        'title':'Iniciar Sesion'
    }

    return render(request, 'usuarios/login.html',data)

def register(request):
    data = {
        'title':'Crear Cuenta'
    }

    return render(request, 'usuarios/register.html',data)