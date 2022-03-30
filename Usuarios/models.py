from django.db import models
from django.forms import CharField

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    nomUsuario = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=50)
    correo = models.CharField(max_length=50,unique=True)
    edad = models.PositiveIntegerField()
    telefono = models.PositiveIntegerField()

    def __str__(self):
        return self.nomUsuario
