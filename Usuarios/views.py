from django.shortcuts import render
from django.shortcuts import render
from .models import Usuario
from rest_framework import generics
from .serializers import UsuarioSerializer

#
# Create your views here. USUARIOS
#
class UsuarioCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new Usuario
    queryset = Usuario.objects.all(),
    serializer_class = UsuarioSerializer

class UsuarioList(generics.ListAPIView):
    # API endpoint that allows Usuario to be viewed.
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single Usuario by pk.
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a Usuario record to be updated.
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a Usuario record to be deleted.
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
