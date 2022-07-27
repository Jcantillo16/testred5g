from django.urls import path
from django.urls import path
from .views import NoticiaList, NoticiaDetail

urlpatterns = [
    path('noticias/', NoticiaList.as_view(), name='list'),
    path('noticia/<int:pk>/', NoticiaDetail.as_view(), name='detail'),
]
