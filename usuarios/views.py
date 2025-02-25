from django.shortcuts import render, redirect
from django.http import JsonResponse,HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistroUsuarioForm
from .models import Usuario

# Registro de usuarios
def register(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = RegistroUsuarioForm()
    return render(request, "usuarios/register.html", {"form": form})

# Inicio de sesión
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(f"username {username} pass {password}")
        if user is not None:
            print(f"✅ Usuario autenticado: {user}")  # Debug
            login(request, user)
            return redirect("profile")  # Redirige al perfil
        else:
            print("❌ Error: Usuario o contraseña incorrectos")  # Debug
            return HttpResponse("Usuario o contraseña incorrectos")  # Debug
    return render(request, "usuarios/login.html")

# Cierre de sesión
def user_logout(request):
    logout(request)
    return redirect('login')



# Perfil del usuario (protegido)
@login_required
def profile(request):
    return render(request, "usuarios/profile.html", {"user": request.user})
