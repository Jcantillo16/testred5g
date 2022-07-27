from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Noticia
from .serializers import NoticiaSeralizer
from apps.users.models import Usuario
from apps.users.registro import Login
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from apps.users.serializers import UsuarioSerializer, LoginSerializer


# Create your views here.
class NoticiaList(APIView):

    def get(self, request):
        noticias = Noticia.objects.all()
        serializer = NoticiaSeralizer(noticias, many=True)
        return Response(serializer.data)

    def post(self, request):
        login = Login()
        if login:
            serializer = NoticiaSeralizer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        return Response({'message': 'Invalid credentials'}, status=400)


class NoticiaDetail(APIView):

    def get(self, request, pk=None):
        noticia = Noticia.objects.get(pk=pk)
        serializer = NoticiaSeralizer(noticia)
        return Response(serializer.data)

    def put(self, request, pk=None):
        noticia = Noticia.objects.get(pk=pk)
        serializer = NoticiaSeralizer(noticia, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk=None):
        noticia = Noticia.objects.get(pk=pk)
        noticia.delete()
        return Response(status=204)
