from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario 
        fields = ['pk', 'nombre', 'nomUsuario', 'password', 'correo', 'edad', 'telefono']
