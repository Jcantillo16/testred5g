from rest_framework import serializers
from .models import Noticia
from apps.comentarios.models import Comentario
from apps.comentarios.serializers import ComentarioSerializer


class NoticiaSeralizer(serializers.ModelSerializer):
    comentario = ComentarioSerializer(many=True, read_only=True)

    class Meta:
        model = Noticia
        fields = '__all__'
