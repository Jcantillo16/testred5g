from django.urls import path
from .views import ComentarioList, ComentarioDetail

urlpatterns = [
    path('comentarios/', ComentarioList.as_view(), name='comentario_list'),
    path('comentario/<int:pk>/', ComentarioDetail.as_view(), name='comentario_detail'),
]
