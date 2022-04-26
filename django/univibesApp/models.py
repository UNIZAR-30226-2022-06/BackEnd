from django.db import models

# Create your models here.

class Documento(models.Model):
    nombre = models.CharField(max_length=50)
    formato = models.CharField(max_length=5)
    linkDocumento = models.CharField(max_length=500)
    #autor = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.nombre

class Libro(Documento):
    linkPortada = models.CharField(max_length=500)
    autor = models.CharField(max_length=100)

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    nomUsuario = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=50)
    correo = models.CharField(max_length=50,unique=True)
    esAdmin = models.BooleanField()
    docsAnyadidos = models.ManyToManyField(Libro,related_name='+')
    docsSubidos = models.ManyToManyField(Documento,related_name='+')
    #Configuracion
    letraSize = models.PositiveIntegerField(null=True,blank=True)
    letraStyle = models.CharField(max_length=30,null=True,blank=True)
    colorFondo = models.CharField(max_length=30,null=True,blank=True)
    def __str__(self):
        return self.nomUsuario

class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    pagina = models.PositiveIntegerField()
    offset = models.PositiveIntegerField()
    esUltimaLeida = models.BooleanField()
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro,on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre