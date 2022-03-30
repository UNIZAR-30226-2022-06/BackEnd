from django.urls import include, path
from . import views

urlpatterns = [
    path('create/', views.UsuarioCreate.as_view(), name='create-usuario'),
    path('', views.UsuarioList.as_view()),
    path('<int:pk>/', views.UsuarioDetail.as_view(), name='retrieve-usuario'),
    path('update/<int:pk>/', views.UsuarioUpdate.as_view(), name='update-usuario'),
    path('delete/<int:pk>/', views.UsuarioDelete.as_view(), name='delete-usuario')
]