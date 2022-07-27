from django.urls import path
from .views import UsuarioList
from .registro import Registro, Login, Logout, UsuarioList

urlpatterns = [
    path('usuarios/', UsuarioList.as_view(), name='list'),
    path('registro/', Registro.as_view(), name='registro'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('usuarios/', UsuarioList.as_view(), name='list'),


]
