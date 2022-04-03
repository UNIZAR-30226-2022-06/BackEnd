from django.db import models

# Create your models here.

class Documento(models.Model):
    nombre = models.CharField(max_length=50)
    formato = models.CharField(max_length=5)
    linkDocumento = models.CharField(max_length=500)
    def __str__(self):
        return self.nombre

# class Autor(models.Model):
#     nombre = models.CharField(max_length=50)
#     def __str__(self):
#         return self.nombre

class Libro(Documento):
    ISBN = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=5000)
    autor = models.CharField(max_length=100)
    #autor = models.ManyToManyField(Autor)
    #linkPortada = models.CharField(max_length=500)

class Configuracion(models.Model):
    letraSize = models.PositiveIntegerField()
    letraStyle = models.CharField(max_length=30)
    colorFondo = models.CharField(max_length=30)

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    nomUsuario = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=50)
    correo = models.CharField(max_length=50,unique=True)
    esAdmin = models.BooleanField()
    #telefono = models.PositiveIntegerField()
    #configuracion = models.OneToOneField(Configuracion,related_name='usuario',on_delete=models.CASCADE,null=True)
    docsAnyadidos = models.ManyToManyField(Documento,related_name='+')
    docsSubidos = models.ManyToManyField(Documento,related_name='+')
    def __str__(self):
        return self.nomUsuario

class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    pagina = models.PositiveIntegerField()
    offset = models.PositiveIntegerField()
    esUltimaLeida = models.BooleanField()
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    documento = models.ForeignKey(Documento,on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre