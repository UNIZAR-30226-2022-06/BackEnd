from django.urls import include, path
from .views import UsuarioCreate, UsuarioList, UsuarioDetail, UsuarioDetailCorreo, UsuarioUpdate, UsuarioAddDocs, UsuarioDeleteDocs, UsuarioDelete, UsuarioDetailCorreo, EnviarCorreoView, UsuarioLogin
from .views import DocumentoCreate, DocumentoList, DocumentoDetail, DocumentoUpdate, DocumentoDelete
from .views import LibroCreate, LibroList, LibroDetail, LibroUpdate, LibroDelete, LibroListPage, ValorarLibro
from .views import MarcaCreate, MarcaList, MarcaDetail, MarcaUpdate, MarcaDelete, LeerLibro

urlpatterns = [
    path('createUsuario/', UsuarioCreate.as_view(), name='create-usuario'),
    path('Usuarios/', UsuarioList.as_view(), name='list-Usuarios'),
    path('Usuarios/<str:nomUsuario>/', UsuarioDetail.as_view(), name='retrieve-usuario'),
    path('Login/<str:nomUsuario>/', UsuarioLogin.as_view(), name='login'),
    path('UsuariosCorreo/<str:correo>/', UsuarioDetailCorreo.as_view(), name='retrieve-usuario-correo'),
    path('enviarCorreo/<str:correo>/', EnviarCorreoView.as_view(), name='enviar-correo'),
    path('updateUsuario/<str:nomUsuario>/', UsuarioUpdate.as_view(), name='update-usuario'),
    path('addDocsUsuario/<str:nomUsuario>/', UsuarioAddDocs.as_view(), name='addDocs-usuario'),
    path('deleteDocUsuario/<str:nomUsuario>/', UsuarioDeleteDocs.as_view(), name='delDoc-usuario'),
    path('deleteUsuario/<str:nomUsuario>/', UsuarioDelete.as_view(), name='delete-usuario'),
    path('createDocumento/', DocumentoCreate.as_view(), name='create-Documento'),
    path('Documentos/', DocumentoList.as_view(), name='list-Documentos'),
    path('Documentos/<str:nombre>/', DocumentoDetail.as_view(), name='retrieve-Documento'),
    path('updateDocumento/<int:pk>/', DocumentoUpdate.as_view(), name='update-Documento'),
    path('deleteDocumento/<int:pk>/', DocumentoDelete.as_view(), name='delete-Documento'),
    path('createLibro/', LibroCreate.as_view(), name='create-Libro'),
    path('Libros/', LibroList.as_view(), name='list-Libros'),
    path('LibrosPage/', LibroListPage.as_view(), name='list-Libros'),
    #path('Libros/<int:pk>/', LibroDetail.as_view(), name='retrieve-Libro-id'),
    path('Libros/<str:nombre>/', LibroDetail.as_view(), name='retrieve-Libro-nombre'),
    path('updateLibro/<str:nombre>/', LibroUpdate.as_view(), name='update-Libro'),
    path('valorarLibro/<str:nombre>/', ValorarLibro.as_view(), name='valorar-Libro'),
    path('deleteLibro/<str:nombre>/', LibroDelete.as_view(), name='delete-Libro'),
    path('createMarca/', MarcaCreate.as_view(), name='create-Marca'),
    path('Marcas/', MarcaList.as_view(), name='list-Marcas'),
    path('Marcas/<int:pk>/', MarcaDetail.as_view(), name='retrieve-Marca'),
    path('updateMarca/<int:pk>/', MarcaUpdate.as_view(), name='update-Marca'),
    path('deleteMarca/<int:pk>/', MarcaDelete.as_view(), name='delete-Marca'),

    path('leerLibro/<str:nombre>/<int:pagina>', LeerLibro.as_view()),

]
