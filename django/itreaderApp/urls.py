from django.urls import include, path
from .views import BorrarLibroUsuario, CompartirLibro, DocumentoListUsuario, LeerLibroUsuario, LibrosUser, MarcaDeleteAll, MarcaDeleteId, MarcaListUsuarioLibro, MarcaUpdateAndroid, Marcapaginas, UsuarioCreate, UsuarioDeleteDocsId, UsuarioDeleteLibro, UsuarioList, UsuarioDetail, UsuarioDetailCorreo, UsuarioUpdate, UsuarioAddDocs, UsuarioDeleteDocs, UsuarioDelete, UsuarioDetailCorreo, EnviarCorreoView, UsuarioLogin, upload_file2
from .views import DocumentoCreate, DocumentoList, DocumentoDetail, DocumentoUpdate, DocumentoDelete, MarcaListUsuario
from .views import LibroCreate, LibroList, LibroDetail, LibroUpdate, LibroDelete, LibroListPage, ValorarLibro
from .views import MarcaCreate, MarcaList, MarcaDetail, MarcaUpdate, MarcaDelete, LeerLibro, upload_file, LeerLibroWeb, LeerLibroUsuarioWeb

urlpatterns = [
    path('createUsuario/', UsuarioCreate.as_view(), name='create-usuario'),
    path('Usuarios/', UsuarioList.as_view(), name='list-Usuarios'),
    path('Usuarios/<str:nomUsuario>/', UsuarioDetail.as_view(), name='retrieve-usuario'),
    path('Login/<str:nomUsuario>/', UsuarioLogin.as_view(), name='login'),
    path('UsuariosCorreo/<str:correo>/', UsuarioDetailCorreo.as_view(), name='retrieve-usuario-correo'),
    path('enviarCorreo/<str:correo>/', EnviarCorreoView.as_view(), name='enviar-correo'),
    path('compartirLibro/<str:usuario>/<str:libro>/<str:correo>/', CompartirLibro.as_view(), name='compartir-libro'),
    path('updateUsuario/<str:nomUsuario>/', UsuarioUpdate.as_view(), name='update-usuario'),
    path('addDocsUsuario/<str:nomUsuario>/', UsuarioAddDocs.as_view(), name='addDocs-usuario'),
    path('deleteDocUsuario/<str:nomUsuario>/', UsuarioDeleteDocs.as_view(), name='delDoc-usuario'),
    path('deleteDocUsuarioId/<str:nomUsuario>/', UsuarioDeleteDocsId.as_view(), name='delDoc-usuario'),
    path('deleteLibroUsuario/<str:nomUsuario>/', UsuarioDeleteLibro.as_view(), name='delLibro-usuario'),
    path('deleteUsuario/<str:nomUsuario>/', UsuarioDelete.as_view(), name='delete-usuario'),
    path('createDocumento/', DocumentoCreate.as_view(), name='create-Documento'),
    path('Documentos/', DocumentoList.as_view(), name='list-Documentos'),
    path('Documentos/<str:nombre>/', DocumentoDetail.as_view(), name='retrieve-Documento'),
    path('DocumentosUser/<str:nombre>/', DocumentoListUsuario.as_view(), name='list-DocumentosUser'),
    path('updateDocumento/<int:pk>/', DocumentoUpdate.as_view(), name='update-Documento'),
    path('deleteDocumento/<int:pk>/', DocumentoDelete.as_view(), name='delete-Documento'),
    path('createLibro/', LibroCreate.as_view(), name='create-Libro'),
    path('Libros/', LibroList.as_view(), name='list-Libros'),
    path('LibrosPage/', LibroListPage.as_view(), name='list-Libros'),
    #path('Libros/<int:pk>/', LibroDetail.as_view(), name='retrieve-Libro-id'),
    path('Libros/<str:nombre>/', LibroDetail.as_view(), name='retrieve-Libro-nombre'),
    path('LibrosUser/<str:usuario>/', LibrosUser.as_view(), name='list-libros-usuario'),
    path('updateLibro/<str:nombre>/', LibroUpdate.as_view(), name='update-Libro'),
    path('valorarLibro/<str:nombre>/', ValorarLibro.as_view(), name='valorar-Libro'),
    path('deleteLibro/<str:nombre>/', LibroDelete.as_view(), name='delete-Libro'),
    path('createMarca/', MarcaCreate.as_view(), name='create-Marca'),
    path('Marcas/', MarcaList.as_view(), name='list-Marcas'),
    path('MarcaPaginas/<str:nomUsuario>/<str:nomLibro>/', Marcapaginas.as_view(), name='list-Marcas'),
    path('Marcas/<str:nombre>/', MarcaDetail.as_view(), name='retrieve-Marca'),
    path('MarcasUsuario/<str:nomUsuario>/', MarcaListUsuario.as_view(), name='retrieve-Marcas-Usuario'),
    path('MarcasUsuarioLibro/<str:nomUsuario>/<str:nomLibro>/', MarcaListUsuarioLibro.as_view(), name='retrieve-Marcas-Libro'),
    path('updateMarca/<str:nombre>/', MarcaUpdate.as_view(), name='update-Marca'),
    path('updateMarcaAndroid/<str:nomUsuario>/<str:nomLibro>/', MarcaUpdateAndroid.as_view(), name='update-Marca-android'),
    path('deleteMarca/<str:nomUsuario>/<int:idLibro>/<str:nomMarca>/', MarcaDelete.as_view(), name='delete-Marca'),
    path('deleteMarcas/<str:nombre>/', MarcaDeleteAll.as_view(), name='delete-Marca'),
    path('deleteMarcas/<int:id>/', MarcaDeleteId.as_view(), name='delete-Marca-id'),

    path('leerLibro/<str:nombre>/<int:pagina>', LeerLibro.as_view()),
    path('leerLibro/<str:usuario>/<str:nombre>/<int:pagina>', LeerLibroUsuario.as_view()),
    path('subirLibro/', upload_file.as_view()),
    path('subirLibro2/<str:filename>/', upload_file2.as_view()),
    path('borrarLibro/<str:usuario>/<str:nombre>', BorrarLibroUsuario.as_view()),
    path('leerLibroWeb/<str:nombre>/', LeerLibroWeb.as_view()),
    path('leerLibroWeb/<str:usuario>/<str:nombre>/', LeerLibroUsuarioWeb.as_view()),

]
