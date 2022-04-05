from django.urls import include, path
from .views import UsuarioCreate, UsuarioList, UsuarioDetail, UsuarioUpdate, UsuarioAddDocs, UsuarioDelete
from .views import ConfiguracionCreate, ConfiguracionList, ConfiguracionDetail, ConfiguracionUpdate, ConfiguracionDelete
from .views import DocumentoCreate, DocumentoList, DocumentoDetail, DocumentoUpdate, DocumentoDelete
from .views import LibroCreate, LibroList, LibroDetail, LibroUpdate, LibroDelete
from .views import MarcaCreate, MarcaList, MarcaDetail, MarcaUpdate, MarcaDelete



urlpatterns = [
    path('createUsuario/', UsuarioCreate.as_view(), name='create-usuario'),
    path('Usuarios', UsuarioList.as_view()),
    path('Usuarios/<str:nomUsuario>/', UsuarioDetail.as_view(), name='retrieve-usuario'),
    path('Usuarios/<str:correo>/', UsuarioDetail.as_view(), name='retrieve-usuario'),
    path('updateUsuario/<str:nomUsuario>/', UsuarioUpdate.as_view(), name='update-usuario'),
    path('addDocsUsuario/<str:nomUsuario>/', UsuarioAddDocs.as_view(), name='addDocs-usuario'),
    path('deleteUsuario/<str:nomUsuario>/', UsuarioDelete.as_view(), name='delete-usuario'),
    path('createConfiguracion/', ConfiguracionCreate.as_view(), name='create-Configuracion'),
    path('Configuracions', ConfiguracionList.as_view()),
    path('Configuracions/<int:pk>/', ConfiguracionDetail.as_view(), name='retrieve-Configuracion'),
    path('updateConfiguracion/<int:pk>/', ConfiguracionUpdate.as_view(), name='update-Configuracion'),
    path('deleteConfiguracion/<int:pk>/', ConfiguracionDelete.as_view(), name='delete-Configuracion'),
    path('createDocumento/', DocumentoCreate.as_view(), name='create-Documento'),
    path('Documentos', DocumentoList.as_view()),
    path('Documentos/<int:pk>/', DocumentoDetail.as_view(), name='retrieve-Documento'),
    path('updateDocumento/<int:pk>/', DocumentoUpdate.as_view(), name='update-Documento'),
    path('deleteDocumento/<int:pk>/', DocumentoDelete.as_view(), name='delete-Documento'),
    path('createLibro/', LibroCreate.as_view(), name='create-Libro'),
    path('Libros', LibroList.as_view()),
    path('Libros/<int:pk>/', LibroDetail.as_view(), name='retrieve-Libro'),
    path('updateLibro/<int:pk>/', LibroUpdate.as_view(), name='update-Libro'),
    path('deleteLibro/<int:pk>/', LibroDelete.as_view(), name='delete-Libro'),
    path('createMarca/', MarcaCreate.as_view(), name='create-Marca'),
    path('Marcas', MarcaList.as_view()),
    path('Marcas/<int:pk>/', MarcaDetail.as_view(), name='retrieve-Marca'),
    path('updateMarca/<int:pk>/', MarcaUpdate.as_view(), name='update-Marca'),
    path('deleteMarca/<int:pk>/', MarcaDelete.as_view(), name='delete-Marca'),

]
