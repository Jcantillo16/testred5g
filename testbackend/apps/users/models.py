from django.db import models

# Create your models here.

class Usuario (models.Model):
    nombres = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    contraseña = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()

    class Meta:
        db_table = 'usuario'

    def __str__(self):
        return self.nombres



