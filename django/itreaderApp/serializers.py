from secrets import choice
from rest_framework import serializers
from .models import Documento, Libro, Usuario, Marca
from django.contrib.auth.models import User

class DocumentoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Documento
        fields = '__all__'



class LibroSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Libro
        fields = '__all__'


class UsuarioCreateSerializer(serializers.ModelSerializer):
    #configuracion = ConfiguracionSerializer(read_only=True)
    class Meta:
        model = Usuario
        fields = ['nombre', 'nomUsuario', 'password', 'correo', 'esAdmin']
    depth = 1


class UserSerializer(serializers.ModelSerializer):
    #configuracion = ConfiguracionSerializer(read_only=True)
    class Meta:
        model = User
        fields = '__all__'

class UserCreateSerializer(serializers.ModelSerializer):
    #configuracion = ConfiguracionSerializer(read_only=True)
    class Meta:
        model = User
        fields = ['username', 'password', 'email']


class UsuarioSerializer(serializers.ModelSerializer):
    #configuracion = ConfiguracionSerializer(read_only=True)
    docsAnyadidos = DocumentoSerializer(many=True)
    docsSubidos = DocumentoSerializer(many=True)
    class Meta:
        model = Usuario
        fields = '__all__'
    depth = 1


class UsuarioAddDocsSerializer(serializers.ModelSerializer):
    #configuracion = ConfiguracionSerializer(read_only=True)
    docsAnyadidos = DocumentoSerializer(many=True)
    docsSubidos = DocumentoSerializer(many=True)
    class Meta:
        model = Usuario
        fields = '__all__'
    depth = 1
    def update(self, instance, validated_data):
        docs_data_an = validated_data.pop('docsAnyadidos')
        for doc_data in docs_data_an:
            a = Documento.objects.get(nombre=doc_data["nombre"])
            instance.docsAnyadidos.add(a)
            instance.save()
        docs_data_sub = validated_data.pop('docsSubidos')
        for doc_data in docs_data_sub:
            a = Documento.objects.get(nombre=doc_data["nombre"])
            instance.docsSubidos.add(a)
            instance.save()
        return instance

class MarcaSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer
    libro = LibroSerializer
    depth = 1
    class Meta:
        model = Marca
        fields = '__all__'


