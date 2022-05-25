from cgitb import lookup
from pyexpat import model
from django.conf import Settings, SettingsReference, settings
from django.shortcuts import render

from itreaderPr.settings import MEDIA_URL
from .models import Usuario, Documento, Libro, Marca
from rest_framework import generics, status
from .serializers import UsuarioSerializer, UsuarioCreateSerializer, UsuarioAddDocsSerializer, DocumentoSerializer, LibroSerializer, MarcaSerializer, UserSerializer, UserCreateSerializer
from rest_framework.pagination import PageNumberPagination
from django.core.mail import send_mail
from django.http import HttpResponse
from urllib import response
from django.conf import settings
from os import environ
import os
import smtplib
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from utils.operations import traducir_archivo, local_media, busca, subir_archivo, file_id_folder, delete_archivo, borrar_recuperar
from rest_framework import viewsets
from rest_framework.parsers import FileUploadParser
    
class UsuarioLogin(generics.RetrieveAPIView):
    # API endpoint that returns a single Usuario by pk.
    lookup_field = 'nomUsuario'
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    def post(self, request, *args, **kwargs):
        us = Usuario.objects.get(nomUsuario=self.kwargs['nomUsuario'])
        if us.password == request.GET['password']:
        #if check_password(request.GET['password'], us.password):
        #if check_password(request.POST['password'], us.password):
            return self.retrieve(request, *args, **kwargs)
        else:
            response = {}
            response['success'] = False
            response['message'] = "Login no valido"
            response['status'] = status.HTTP_400_BAD_REQUEST
            return Response(response)
         


# Create your views here.

    
#USUARIO

class UsuarioCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new Usuario
    queryset = Usuario.objects.all()
    serializer_class = UsuarioCreateSerializer
    # def post(self, request, *args, **kwargs):
    #     self.create(request, *args, **kwargs)
    #     us = Usuario.objects.get(nomUsuario=request.data['nomUsuario'])
    #     # contrasenya = us.password
    #     # contrasenya2 = make_password(contrasenya)
    #     # us.password = contrasenya2        
    #     if request.data['esAdmin'] == 0:
    #         us.esAdmin = False
    #     else:
    #         us.esAdmin = True
    #     us.save()
    #     response = {}
    #     response['success'] = True
    #     response['message'] = "Registro guardado exitosamente"
    #     response['status'] = status.HTTP_201_CREATED
    #     return Response(response)
        

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

        # contrasena = User.objects.make_random_password()
        # us = Usuario.objects.get(correo=self.kwargs['correo'])
        # us.password = make_password(contrasena)
        # us.save()

        contrasena = Usuario.objects.get(correo=self.kwargs['correo']).password
        
        # contrasena = get_random_string(length=10, allowed_chars='abcde')
        # us = Usuario.objects.get(correo=request.data['correo'])
        # us.password = make_password(contrasena)
        # us.save()

        
        email = self.kwargs['correo']

        #email = self.request.query_params.['correo']
        print('email '+email)

        contrasenya = str(contrasena)
        html = '<h1>Su contraseña es '+contrasenya+'</h1>'
        #text = 'niñería'

        mail = MIMEMultipart('alternative')
        mail['From'] = 'itreadersoftkare@gmail.com'
        mail['To'] = email
        mail['Cc'] = ''
        mail['Subject'] = 'Su contraseña es '+contrasenya

        # Record the MIME types of both parts - text/plain and text/html.
        #part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')

        # Attach parts into message container. According to RFC 2046, the last
        # part of a multipart message, in this case the HTML message, is best
        # and preferred.
        #mail.attach(part1)
        mail.attach(part2)

        msg_full = mail.as_string().encode()

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('itreadersoftkare@gmail.com', 'Proyecto2022')


        
        server.sendmail('itreadersoftkare@gmail.com', email, msg_full)


        server.quit()

        return self.retrieve(request, *args, **kwargs)



class CompartirLibro(generics.RetrieveAPIView):
    # API endpoint that returns a single Usuario by pk..
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def get(self, request, *args, **kwargs):
           
        email = self.kwargs['correo']

        #email = self.request.query_params.['correo']
        print('email '+email)
        split_libro = self.kwargs['libro'].split(".", 1)
        html = '<h1>El usuario '+self.kwargs['usuario']+' te recomienda el libro '+split_libro[0]+', disponible en la aplicación Itreader.</h1>'
        #text = 'niñería'

        mail = MIMEMultipart('alternative')
        mail['From'] = 'itreadersoftkare@gmail.com'
        mail['To'] = email
        mail['Cc'] = ''
        mail['Subject'] = 'Recomendación Itreader'

        # Record the MIME types of both parts - text/plain and text/html.
        #part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')

        # Attach parts into message container. According to RFC 2046, the last
        # part of a multipart message, in this case the HTML message, is best
        # and preferred.
        #mail.attach(part1)
        mail.attach(part2)

        msg_full = mail.as_string().encode()

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('itreadersoftkare@gmail.com', 'Proyecto2022')


        
        server.sendmail('itreadersoftkare@gmail.com', email, msg_full)


        server.quit()

        return self.retrieve(request, *args, **kwargs)



class UsuarioUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a Usuario record to be updated.
    queryset = Usuario.objects.all()
    lookup_field = 'nomUsuario'
    serializer_class = UsuarioCreateSerializer
    def put(self, request, *args, **kwargs):
        #request.data['password'] = make_password(request.data['password'])
        return self.partial_update(request, *args, **kwargs)


class UsuarioAddDocs(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a Usuario record to be updated.
    queryset = Usuario.objects.all()
    lookup_field = 'nomUsuario'
    serializer_class = UsuarioAddDocsSerializer
    def put(self, request, *args, **kwargs):
        us = Usuario.objects.get(nomUsuario=self.kwargs['nomUsuario'])
        lib = Libro.objects.get(nombre=request.data['nomLibro'])
        beforeInsert = us.docsAnyadidos.all().count()
        us.docsAnyadidos.add(lib)
        afterInsert = us.docsAnyadidos.all().count()
        if (beforeInsert+1) != afterInsert:
            return Response({'message': 'ERROR: No se ha añadido'}, status=status.HTTP_409_CONFLICT)
        else:
            nom = "Marcapaginas"+request.data['nomLibro']
            Marca.objects.create(nombre=nom,pagina=1,offset=0,esUltimaLeida=True,usuario=us,libro=lib)
            return Response({'message': 'Se ha añadido correctamente'}, status=status.HTTP_200_OK)



class UsuarioDeleteLibro(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a Usuario record to be updated.
    queryset = Usuario.objects.all()
    lookup_field = 'nomUsuario'
    serializer_class = UsuarioAddDocsSerializer
    def put(self, request, *args, **kwargs):      
        lib = Libro.objects.get(nombre=request.data['nomLibro'])
        us = Usuario.objects.get(nomUsuario=self.kwargs['nomUsuario']) 
        beforeInsert = us.docsAnyadidos.all().count()
        us.docsAnyadidos.remove(lib)
        afterInsert = us.docsAnyadidos.all().count()
        if beforeInsert == afterInsert:
            return Response({'message': 'ERROR: No se ha borrado'}, status=status.HTTP_409_CONFLICT)
        else:
            marca = Marca.objects.get(usuario=us,libro=lib,esUltimaLeida=True)
            marca.delete()
            return Response({'message': 'Se ha borrado correctamente'}, status=status.HTTP_200_OK)


class UsuarioDeleteDocs(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a Usuario record to be updated.
    queryset = Usuario.objects.all()
    lookup_field = 'nomUsuario'
    serializer_class = UsuarioAddDocsSerializer
    def put(self, request, *args, **kwargs):      
        doc = Documento.objects.get(nombre=request.data['nomLibro'])
        usuario = Usuario.objects.get(nomUsuario=self.kwargs['nomUsuario']) 
        beforeInsert = usuario.docsAnyadidos.all().count()
        usuario.docsSubidos.remove(doc)
        afterInsert = usuario.docsAnyadidos.all().count()
        doc.delete()
        if beforeInsert == afterInsert:
            return Response({'message': 'ERROR: No se ha borrado'}, status=status.HTTP_409_CONFLICT)
        else:
            return Response({'message': 'Se ha borrado correctamente'}, status=status.HTTP_200_OK)

       
class UsuarioDeleteDocsId(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a Usuario record to be updated.
    queryset = Usuario.objects.all()
    lookup_field = 'nomUsuario'
    serializer_class = UsuarioAddDocsSerializer
    def put(self, request, *args, **kwargs):      
        doc = Documento.objects.get(id=request.data['id'])
        usuario = Usuario.objects.get(nomUsuario=self.kwargs['nomUsuario']) 
        beforeInsert = usuario.docsAnyadidos.all().count()
        usuario.docsSubidos.remove(doc)
        afterInsert = usuario.docsAnyadidos.all().count()
        doc.delete()
        if beforeInsert == afterInsert:
            return Response({'message': 'ERROR: No se ha borrado'}, status=status.HTTP_409_CONFLICT)
        else:
            return Response({'message': 'Se ha borrado correctamente'}, status=status.HTTP_200_OK)



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
    lookup_field = 'nombre'

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

class DocumentoListUsuario(generics.ListAPIView):
    # API endpoint that allows Documento to be viewed.
    model = Documento
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer
    def get_queryset(self):
        nom = "_"+self.kwargs['nombre']
        return Documento.objects.filter(nombre__endswith=nom)


#Libro

class LibroCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new Libro
    queryset = Libro.objects.all(),
    serializer_class = LibroSerializer
 
class LibroList(generics.ListAPIView):
    # API endpoint that allows Libro to be viewed.
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    # def get_queryset(self):
    #     return Libro.objects.all().order_by('nombre')


class SmallResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_query_param = 'page'

class LibroListPage(generics.ListAPIView):
    # API endpoint that allows Libro to be viewed.
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    pagination_class = SmallResultsSetPagination

class LibroDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single Libro by pk.
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    lookup_field = 'nombre'

class LibroUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a Libro record to be updated.
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    lookup_field = 'nombre'
    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class LibroDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a Libro record to be deleted.
    queryset = Libro.objects.all()
    lookup_field = 'nombre'
    serializer_class = LibroSerializer

class LibrosUser(generics.ListAPIView):
    # API endpoint that allows a Libro record to be deleted.
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    def get_queryset(self):
        us = Usuario.objects.get(nomUsuario=self.kwargs['usuario'])
        return us.docsAnyadidos.all()


class ValorarLibro(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a Usuario record to be updated.
    queryset = Libro.objects.all()
    lookup_field = 'nombre'
    serializer_class = LibroSerializer
    def put(self, request, *args, **kwargs):
        libro = Libro.objects.get(nombre=self.kwargs['nombre'])
        request.data['numValoraciones'] = libro.numValoraciones + 1
        request.data['valoracion'] = ((libro.valoracion*(libro.numValoraciones))+request.data['valoracion'])/request.data['numValoraciones']
        return self.partial_update(request, *args, **kwargs)


#Marca

class MarcaCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new Marca
    queryset = Marca.objects.all(),
    serializer_class = MarcaSerializer

    def post(self, request, *args, **kwargs):
        us = Usuario.objects.get(nomUsuario=request.data['usuario'])
        lib = Libro.objects.get(nombre=request.data['libro'])

        marcas = Marca.objects.filter(usuario=us.id,libro=lib.id,esUltimaLeida=False).count()

        if marcas < 15:
            esUlt = None
            if request.data['esUlt'] == 0:
                esUlt = False
            else:
                esUlt = True
            Marca.objects.create(nombre=request.data['nombre'],pagina=request.data['pagina'],offset=0,esUltimaLeida=esUlt,usuario=us,libro=lib)
            response = {}
            response['success'] = True
            response['message'] = "Marca creada exitosamente"
            response['status'] = status.HTTP_201_CREATED
            return Response(response)
        else:
            response = {}
            response['success'] = False
            response['message'] = "Marca no creada"
            response['status'] = status.HTTP_400_BAD_REQUEST
            return Response(response)

class MarcaList(generics.ListAPIView):
    # API endpoint that allows Marca to be viewed.
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class MarcaListUsuario(generics.ListAPIView):
    # API endpoint that allows a Libro record to be updated.
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

    #def list(self, request, *args, **kwargs):
        # ev = Libro.objects.get(nombre=self.kwargs['nombre'])
        # us = Usuario.objects.get(nomUsuario=self.kwargs['username'])
        # queryset = self.filter_queryset((self.get_queryset()).filter(usuario=us))
        # page = self.paginate_queryset(queryset)
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)
        # else:
        #     serializer = self.get_serializer(queryset, many=True)
        #     return Response(serializer.data)
    def get_queryset(self):
        us = Usuario.objects.get(nomUsuario=self.kwargs['nomUsuario'])
        return Marca.objects.filter(usuario=us.id)

class MarcaListUsuarioLibro(generics.ListAPIView):
    # API endpoint that allows a Libro record to be updated.
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

    #def list(self, request, *args, **kwargs):
        # ev = Libro.objects.get(nombre=self.kwargs['nombre'])
        # us = Usuario.objects.get(nomUsuario=self.kwargs['username'])
        # queryset = self.filter_queryset((self.get_queryset()).filter(usuario=us))
        # page = self.paginate_queryset(queryset)
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)
        # else:
        #     serializer = self.get_serializer(queryset, many=True)
        #     return Response(serializer.data)
    def get_queryset(self):
        us = Usuario.objects.get(nomUsuario=self.kwargs['nomUsuario'])
        lib = Libro.objects.get(nombre=self.kwargs['nomLibro'])
        return Marca.objects.filter(usuario=us.id,libro=lib.id,esUltimaLeida=False)

    

class MarcaDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single Marca by pk.
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    lookup_field = "nombre"

class Marcapaginas(generics.ListAPIView):
    # API endpoint that returns a single Marca by pk.
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    def get_queryset(self):
        us = Usuario.objects.get(nomUsuario=self.kwargs['nomUsuario'])
        l = Libro.objects.get(nombre=self.kwargs['nomLibro'])
        return Marca.objects.filter(usuario=us,libro=l,esUltimaLeida=True)

class MarcaUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a Marca record to be updated.
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    lookup_field = "nombre"
    def put(self, request, *args, **kwargs):
        # us = Usuario.objects.get(nomUsuario=request.data['usuario'])
        # lib = Libro.objects.get(nombre=request.data['libro'])
        # esUlt = None
        # if request.data['esUltimaLeida'] == 0:
        #     request.data['esUltimaLeida'] = False
        # else:
        #     request.data['esUltimaLeida'] = True
        # request.data['usuario'] = us.id
        # request.data['libro'] = lib.id
        return self.partial_update(request, *args, **kwargs)

    
class MarcaUpdateAndroid(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a Marca record to be updated.
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    lookup_field = "nombre"
    def put(self, request, *args, **kwargs):
        us = Usuario.objects.get(nomUsuario=self.kwargs['nomUsuario'])
        l = Libro.objects.get(nombre=self.kwargs['nomLibro'])
        m = Marca.objects.get(usuario=us.id,libro=l.id,esUltimaLeida=True)
        m.pagina = request.data['pagina']
        m.save()
        response = {}
        response['success'] = True
        response['message'] = "Marca actualizada exitosamente"
        response['status'] = status.HTTP_201_CREATED
        return Response(response)


class MarcaDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a Marca record to be deleted.
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    lookup_field = "nombre"
    def delete(self, request, *args, **kwargs):
        us = Usuario.objects.get(nomUsuario=self.kwargs['nomUsuario'])
        l = Libro.objects.get(id=self.kwargs['idLibro'])
        m = Marca.objects.get(usuario=us,libro=l,nombre=self.kwargs['nomMarca'])
        m.delete()
        response = {}
        response['success'] = True
        response['message'] = "Marca borrada exitosamente"
        response['status'] = status.HTTP_201_CREATED
        return Response(response)

class MarcaDeleteAll(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a Marca record to be deleted.
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    lookup_field = "nombre"
    def delete(self, request, *args, **kwargs):
        return Marca.objects.all.delete()

class MarcaDeleteId(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a Marca record to be deleted.
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    lookup_field = "id"
    
#       
# NUEVO
#
class LeerLibro(generics.ListAPIView):
    # API endpoint that allows a Libro record to be updated.
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

    def get(self, request, *args, **kwargs):
        nombre=self.kwargs['nombre'] # libro.epub o libro.pdf
        pagina=self.kwargs['pagina']
        split_archivo = nombre.split(".", 1)
        if(split_archivo[1]=='epub'):
            contenido=traducir_archivo(nombre,pagina,local_media)
            if contenido == 'ERROR':
                contenido = 'ERROR: EPUB no existente'
        elif(split_archivo[1]=='pdf'):
            query = 'title = \'' + nombre + '\' and trashed = false'
            f = busca(query) #"title = 'prueba.pdf'"
            if f == []:
                contenido = 'ERROR: PDF no existente'
            else:
                contenido = f[0]['embedLink']
        else:
            contenido = 'ERROR: Formato no existente'
        return Response({'libro': nombre, 
                        'pagina': pagina,
                        'contenido': contenido}, status=status.HTTP_200_OK)

class upload_file2(generics.ListAPIView):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer
    parser_classes = (FileUploadParser,)
    
    def post(self, request, filename, format=None):
        #file_obj.name == str(cover)
        #file_obj == cover

        file_obj = request.data['file']
        #file_name = request.GET['filename']
        
        usuario = request.GET['usuario']
        #cover = request.data['cover']
        split_archivo = file_obj.name.split(".", 1)
        #split_archivo = str(cover).split(".", 1)

        usuarioObj = Usuario.objects.get(nomUsuario=usuario)
        if usuarioObj.esAdmin:
            doc = Libro.objects.create(linkPortada=str(file_obj),
                autor='David',editorial='Planeta', coverLib=file_obj, valoracion=0, numValoraciones=0,nombre=(split_archivo[0]+'_'+usuario),formato=split_archivo[1],linkDocumento='a', cover=file_obj)
            subir_archivo(file_obj.name,file_id_folder,local_media)
            delete_archivo(file_obj.name, local_media)
            return HttpResponse({'message': 'Book created'}, status=200)
        else:
            doc = Documento.objects.create(nombre=(split_archivo[0]+'_'+usuario),formato=split_archivo[1],linkDocumento='a', cover=file_obj)
            # doc.cover.name = file_name
            # doc.save()
            usuarioObj.docsSubidos.add(doc)
            new_name = split_archivo[0]+'_'+usuario+'.'+split_archivo[1]
            os.rename(local_media+file_obj.name, local_media+new_name)
            subir_archivo(new_name,file_id_folder,local_media)
            delete_archivo(new_name, local_media)
            return HttpResponse({'message': 'Book created'}, status=200)


class upload_file(generics.ListAPIView):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer
    
    def post(self, request, *args, **kwargs):
        
        usuario = request.data['usuario']
        cover = request.data['cover']
        split_archivo = str(cover).split(".", 1)
 
        usuarioObj = Usuario.objects.get(nomUsuario=usuario)
        if usuarioObj.esAdmin:
            doc = Libro.objects.create(linkPortada='https://db-itreader-unizar.herokuapp.com/media/portada.jpg', nombre=str(cover),
                autor='David',editorial='Planeta', coverLib=cover, valoracion=0, numValoraciones=0)
            subir_archivo(str(cover),file_id_folder,local_media)
            delete_archivo(str(cover), local_media)
            return HttpResponse({'message': 'Book created'}, status=200)
        else:
            docs = Documento.objects.filter(nombre=(split_archivo[0]+'_'+usuario))
            if docs:
                return HttpResponse({'message': 'Book not created'}, status=409)
            else: 
                doc = Documento.objects.create(nombre=(split_archivo[0]+'_'+usuario),formato=split_archivo[1],linkDocumento='Documento PDF', cover=cover)
                usuarioObj.docsSubidos.add(doc)
                new_name = split_archivo[0]+'_'+usuario+'.'+split_archivo[1]
                os.rename(local_media+str(cover), local_media+new_name)
                subir_archivo(new_name,file_id_folder,local_media)
                delete_archivo(new_name, local_media)
                return HttpResponse({'message': 'Book created'}, status=200)


class LeerLibroUsuario(generics.ListAPIView):
    # API endpoint that allows a Libro record to be updated.
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

    def get(self, request, *args, **kwargs):
        usuario=self.kwargs['usuario']
        nom=self.kwargs['nombre'] # libro.epub o libro.pdf
        pagina=self.kwargs['pagina']
        split_archivo = nom.split(".", 1)
        nombre = split_archivo[0]+'_'+usuario+'.'+split_archivo[1]
        if(split_archivo[1]=='epub'):
            contenido=traducir_archivo(nombre,pagina,local_media)
            if contenido == 'ERROR':
                contenido = 'ERROR: EPUB no existente'
        elif(split_archivo[1]=='pdf'):
            query = 'title = \'' + nombre + '\' and trashed = false'
            f = busca(query) #"title = 'prueba.pdf'"
            if f == []:
                contenido = 'ERROR: PDF no existente'
            else:
                contenido = f[0]['embedLink']
        else:
            contenido = 'ERROR: Formato no existente'
        return Response({'libro': nom, 
                        'pagina': pagina,
                        'contenido': contenido}, status=status.HTTP_200_OK)

class BorrarLibroUsuario(generics.ListAPIView):
    # API endpoint that allows a Libro record to be updated.
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

    def get(self, request, *args, **kwargs):
        usuario = request.data['usuario']
        nom=self.kwargs['nombre'] # libro.epub o libro.pdf
        usuarioObj = Usuario.objects.get(nomUsuario=usuario)
        if usuarioObj.esAdmin:
            Libro.objects.filter(linkPortada=nom).delete()
            borrar_recuperar(nombre)
            return HttpResponse({'message': 'Book deleted'}, status=200)
        else:
            split_archivo = nom.split(".", 1)
            nombre = split_archivo[0]+'_'+usuario+'.'
            usuarioObj.docsSubidos.filter(linkPortada=nom).delete()
            new_name = split_archivo[0]+'_'+usuario+'.'+split_archivo[1]
            borrar_recuperar(new_name)
            return HttpResponse({'message': 'Book deleted'}, status=200)

class LeerLibroWeb(generics.ListAPIView):
    # API endpoint that allows a Libro record to be updated.
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

    def get(self, request, *args, **kwargs):
        nombre=self.kwargs['nombre'] # libro.epub o libro.pdf
        query = 'title = \'' + nombre + '\' and trashed = false'
        f = busca(query) #"title = 'prueba.pdf'"
        if f == []:
            contenido = 'ERROR: Archivo no existente'
        else:
                contenido = f[0]['embedLink']
        return Response({'libro': nombre,
                        'contenido': contenido}, status=status.HTTP_200_OK)

class LeerLibroUsuarioWeb(generics.ListAPIView):
    # API endpoint that allows a Libro record to be updated.
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

    def get(self, request, *args, **kwargs):
        usuario=self.kwargs['usuario']
        nom=self.kwargs['nombre'] # libro.epub o libro.pdf
        split_archivo = nom.split(".", 1)
        nombre = split_archivo[0]+'_'+usuario+'.'+split_archivo[1]
        query = 'title = \'' + nombre + '\' and trashed = false'
        f = busca(query) #"title = 'prueba.pdf'"
        if f == []:
            contenido = 'ERROR: Archivo no existente'
        else:
                contenido = f[0]['embedLink']
        return Response({'libro': nom, 
                        'contenido': contenido}, status=status.HTTP_200_OK)

