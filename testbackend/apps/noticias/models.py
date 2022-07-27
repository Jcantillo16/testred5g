from django.db import models


# Create your models here.
class Noticia(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)

    class Meta:
        db_table = 'noticia'

    def __str__(self):
        return self.titulo
