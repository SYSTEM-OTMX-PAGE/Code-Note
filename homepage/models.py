from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Proyecto(models.Model):
 usuario = models.ForeignKey(User, on_delete=models.CASCADE)
 nombre = models.CharField(max_length=255)
 descripcion = models.TextField(blank=True)
 fecha_creacion = models.DateTimeField(auto_now_add=True)
 
 def __str__(self):
    return self.nombre