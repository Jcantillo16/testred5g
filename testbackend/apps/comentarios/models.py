from django.db import models
from apps.noticias.models import Noticia


# Create your models here.
class Comentario(models.Model):
    comentario = models.CharField(max_length=50)
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, related_name='comentario', default=None)

    class Meta:
        db_table = 'comentario'

    def __str__(self):
        return self.titulo
