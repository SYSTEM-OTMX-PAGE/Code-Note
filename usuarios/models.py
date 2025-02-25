from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Usuario(AbstractUser):
    foto_perfil = models.ImageField(upload_to='profile_pics/', default='profile_pics/default.jpg')

    # Evitar conflictos con auth.User
    groups = models.ManyToManyField(Group, related_name="usuarios_set", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="usuarios_permissions_set", blank=True)

    def __str__(self):
        return self.username
    
