from secrets import choice
from rest_framework import serializers
from .models import Documento, Autor, Libro, Configuracion, Usuario, Marca

class DocumentoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Documento
        fields = '__all__'

class AutorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Autor
        fields = '__all__'

class LibroSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Libro
        fields = '__all__'

class ConfiguracionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Configuracion
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    configuracion = ConfiguracionSerializer(read_only=True)
    docsAnyadidos = DocumentoSerializer(many=True,read_only=True)
    docsSubidos = DocumentoSerializer(many=True,read_only=True)
    class Meta:
        model = Usuario
        fields = '__all__'

class MarcaSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)
    documento = DocumentoSerializer(read_only=True)
    class Meta:
        model = Marca
        fields = '__all__'

