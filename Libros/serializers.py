from rest_framework import serializers
from .models import Usuario

class LibroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario 
        fields = ['ISBM', 'pathLibro', 'titulo']
