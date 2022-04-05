from django.shortcuts import render
from .models import Usuario, Documento, Libro, Configuracion, Marca
from rest_framework import generics
from .serializers import UsuarioSerializer, UsuarioCreateSerializer, UsuarioAddDocsSerializer, DocumentoSerializer, LibroSerializer, MarcaSerializer, ConfiguracionSerializer

# Create your views here.

#USUARIO

class UsuarioCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new Usuario
    queryset = Usuario.objects.all(),
    serializer_class = UsuarioCreateSerializer
    

class UsuarioList(generics.ListAPIView):
    # API endpoint that allows Usuario to be viewed.
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single Usuario by pk.
    lookup_field = 'nomUsuario'
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
class UsuarioDetailCorreo(generics.RetrieveAPIView):
   # API endpoint that returns a single Usuario by pk.
   lookup_field = 'correo'
   queryset = Usuario.objects.all()
   serializer_class = UsuarioSerializer

class UsuarioUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a Usuario record to be updated.
    queryset = Usuario.objects.all()
    lookup_field = 'nomUsuario'
    serializer_class = UsuarioSerializer
    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class UsuarioAddDocs(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a Usuario record to be updated.
    queryset = Usuario.objects.all()
    lookup_field = 'nomUsuario'
    serializer_class = UsuarioAddDocsSerializer
    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
       
class UsuarioDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a Usuario record to be deleted.
    queryset = Usuario.objects.all()
    lookup_field = 'nomUsuario'
    serializer_class = UsuarioSerializer

#Documento

class DocumentoCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new Documento
    queryset = Documento.objects.all(),
    serializer_class = DocumentoSerializer
 
class DocumentoList(generics.ListAPIView):
    # API endpoint that allows Documento to be viewed.
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer

class DocumentoDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single Documento by pk.
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer

class DocumentoUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a Documento record to be updated.
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer
    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class DocumentoDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a Documento record to be deleted.
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer

#Libro

class LibroCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new Libro
    queryset = Libro.objects.all(),
    serializer_class = LibroSerializer
 
class LibroList(generics.ListAPIView):
    # API endpoint that allows Libro to be viewed.
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

class LibroDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single Libro by pk.
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

class LibroUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a Libro record to be updated.
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class LibroDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a Libro record to be deleted.
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

#Configuracion

class ConfiguracionCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new Configuracion
    queryset = Configuracion.objects.all(),
    serializer_class = ConfiguracionSerializer
 
class ConfiguracionList(generics.ListAPIView):
    # API endpoint that allows Configuracion to be viewed.
    queryset = Configuracion.objects.all()
    serializer_class = ConfiguracionSerializer

class ConfiguracionDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single Configuracion by pk.
    queryset = Configuracion.objects.all()
    serializer_class = ConfiguracionSerializer

class ConfiguracionUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a Configuracion record to be updated.
    queryset = Configuracion.objects.all()
    serializer_class = ConfiguracionSerializer
    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class ConfiguracionDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a Configuracion record to be deleted.
    queryset = Configuracion.objects.all()
    serializer_class = ConfiguracionSerializer


#Marca

class MarcaCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new Marca
    queryset = Marca.objects.all(),
    serializer_class = MarcaSerializer
 
class MarcaList(generics.ListAPIView):
    # API endpoint that allows Marca to be viewed.
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class MarcaDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single Marca by pk.
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class MarcaUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a Marca record to be updated.
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class MarcaDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a Marca record to be deleted.
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer


    
