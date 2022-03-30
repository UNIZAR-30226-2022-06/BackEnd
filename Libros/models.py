from django.db import models

# Create your models here.
class Libro(models.Model):
    ISBM = models.CharField(max_length=20, primary_key=True)
    pathLibro = models.CharField(max_length=200)
    titulo = models.CharField(max_length=50)

    def __str__(self):
        return str(self.titulo)