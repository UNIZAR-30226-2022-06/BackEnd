from secrets import choice
from rest_framework import serializers
from .models import Documento, Libro, Configuracion, Usuario, Marca#, Autor

class DocumentoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Documento
        fields = '__all__'

# class AutorSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Autor
#         fields = '__all__'

class LibroSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Libro
        fields = '__all__'

class ConfiguracionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Configuracion
        fields = '__all__'


class UsuarioCreateSerializer(serializers.ModelSerializer):
    #configuracion = ConfiguracionSerializer(read_only=True)
    class Meta:
        model = Usuario
        fields = ['pk', 'nombre', 'nomUsuario', 'password', 'correo', 'esAdmin']
    depth = 1

class UsuarioSerializer(serializers.ModelSerializer):
    #configuracion = ConfiguracionSerializer(read_only=True)
    docsAnyadidos = DocumentoSerializer(many=True)
    docsSubidos = DocumentoSerializer(many=True)
    class Meta:
        model = Usuario
        fields = '__all__'
    depth = 1
    # def create(self, validated_data):
    #     detail = self.initial_data.get('configuracion')
    #     instance = super().create(validated_data)
    #     if detail:
    #         serializer = ConfiguracionSerializer(data=detail)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save(event=instance)
    #     return instance
    # def update(self, instance, validated_data):
        # for (key, value) in validated_data.items():
        #     setattr(instance, key, value)
        #     instance.save()
        #fields = ['nombre', 'nomUsuario', 'password', 'correo', 'esAdmin']
   

        # for item in validated_data:
        #     if Usuario._meta.get_field(item):
        #         try:
        #             setattr(instance, item, validated_data[item])
        #         except KeyError:  # validated_data may not contain all fields during HTTP PATCH
        #             pass
        # for (key, value) in validated_data.items():
        #     if(key != 'docsAnyadidos' & key != 'docsSubidos'):
        #         try:
        #             setattr(instance, key, value)
        #             instance.save()
        #         except KeyError:  # validated_data may not contain all fields during HTTP PATCH
        #             pass           
        # instance.save()


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
    usuario = UsuarioMarcaSerializer()
    libro = LibroSerializer()
    depth = 1
    class Meta:
        model = Marca
        fields = '__all__'


