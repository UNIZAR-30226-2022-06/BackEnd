from pyexpat import model
from django.conf import Settings, SettingsReference, settings
from django.shortcuts import render
from .models import Usuario, Documento, Libro, Configuracion, Marca
from rest_framework import generics
from .serializers import UsuarioSerializer, UsuarioCreateSerializer, UsuarioAddDocsSerializer, DocumentoSerializer, LibroSerializer, MarcaSerializer, ConfiguracionSerializer
from rest_framework.pagination import PageNumberPagination
from django.core.mail import send_mail
from django.http import HttpResponse
from urllib import response
from django.conf import settings
from os import environ
import smtplib
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText




# Create your views here.

class SmallResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 20
    
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

    # def UsuarioDetailCorreo(self, request, pk_correo, **kwargs):
    #     # Envia el correo de recuperacion de contraseña, si existe el usuario
    #     usuario = Usuario.objects.get(correo=pk_correo)
    #     serializer_class = UsuarioSerializer

    #     contraseña = Usuario.objects.get(correo=self.kwargs['correo'])
    #     email = self.kwargs['correo']

    #     send_mail("Recuperar contraseña","Su contraseña es "+contraseña,"itreadersoftkare@gmail.com",email)


class EnviarCorreoView(generics.RetrieveAPIView):
    # API endpoint that returns a single Usuario by pk..
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def get(self, request, *args, **kwargs):

        #contrasena = Usuario.objects.get(correo=self.kwargs['correo'])
        #email = request['correo']

        # email = self.request.query_params.['correo']
        # print('email'+email)

        # send_mail('Recuperar contraseña','Su contraseña es ','itreadersoftkare@gmail.com',['hectorrute98gp@gmail.com'])

        # return self.retrieve(request, *args, **kwargs)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('itreadersoftkare@gmail.com', 'Proyecto2022')
        server.sendmail('itreadersoftkare@gmail.com', 'hectorrute98gp@gmail.com', 'Mensaje')
        server.quit()

        return self.retrieve(request, *args, **kwargs)



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


# class DocumentoFilter(django_filters.FilterSet):
#     #id = django_filters.NumberFilter()
#     id__gte = django_filters.NumberFilter(field_name='id', lookup_expr='gte')
#     id__lte = django_filters.NumberFilter(field_name='id', lookup_expr='lte')
#     #manufacturer__name = django_filters.CharFilter(lookup_expr='icontains')

#     class Meta:
#         model = Documento
#         fields = ['id']

class DocumentoList(generics.ListAPIView):
    # API endpoint that allows Documento to be viewed.
    model = Documento
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer
    ## filter_backends = (filters.DjangoFilterBackend,)
    # filter_class = DocumentoFilter
    # pagination_class = SmallResultsSetPagination




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


    
