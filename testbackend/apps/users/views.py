from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Usuario
from .serializers import UsuarioSerializer
# Create your views here.


class UsuarioList(APIView):

    def get(self, request):
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


