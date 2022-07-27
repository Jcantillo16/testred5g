from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Comentario
from .serializers import ComentarioSerializer


# Create your views here.
class ComentarioList(APIView):

    def get(self, request):
        comentarios = Comentario.objects.all()
        serializer = ComentarioSerializer(comentarios, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ComentarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class ComentarioDetail(APIView):

    def get(self, request, pk=None):
        comentario = Comentario.objects.get(pk=pk)
        serializer = ComentarioSerializer(comentario)
        return Response(serializer.data)

    def put(self, request, pk=None):
        comentario = Comentario.objects.get(pk=pk)
        serializer = ComentarioSerializer(comentario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk=None):
        comentario = Comentario.objects.get(pk=pk)
        comentario.delete()
        return Response(status=204)
