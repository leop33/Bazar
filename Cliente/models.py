from django.db import models
from Administracion.models import Producto
# Create your models here.
class Cliente(models.Model):
    nombre = models.TextField()
    apellido1 = models.TextField()
    apellido2 = models.TextField()
    email = models.TextField()
    telefono = models.IntegerField()

class RegistroProd(models.Model):
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    visto = models.BooleanField()
    fecha = models.DateField()