
from django.urls import path
from . import views

urlpatterns  = [
    path('login/', views.login , name="usuarios_login"),
    path('register/',views.register, name="usuarios_register")
]