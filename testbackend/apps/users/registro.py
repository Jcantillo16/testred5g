from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Usuario as UsuarioModel
from rest_framework.exceptions import AuthenticationFailed
import jwt
from .serializers import UsuarioSerializer


class Registro(APIView):
    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class Login(APIView):
    def post (self, request):
        email = request.data.get('email')
        contraseña = request.data.get('contraseña')
        try:
            usuario = UsuarioModel.objects.get(email=email, contraseña=contraseña)
        except UsuarioModel.DoesNotExist:
            raise AuthenticationFailed('Invalid credentials')
        payload = {
            'email': usuario.email,
            'nombres': usuario.nombres,
            'id': usuario.id,
        }
        jwt_token = jwt.encode(payload, 'secret', algorithm='HS256')
        return Response({'token': jwt_token})

class Logout(APIView):
    def post(self, request):
        return Response({'message': 'Logged out'})

class UsuarioList(APIView):
    def get(self, request):
        usuarios = UsuarioModel.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)

