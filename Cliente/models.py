from django.db import models
# Create your models here.
def user_directory_path(instance, filename):
    print(f'{filename} guardado')
    if type(instance) == Producto:
        return f'static/Producto/{instance.nombre}.jpg'

class Cliente(models.Model):
    nombre = models.TextField(max_length=45)
    apellido1 = models.TextField(max_length=45)
    apellido2 = models.TextField(max_length=45)
    email = models.TextField()
    telefono = models.IntegerField()
    mensaje = models.TextField(max_length=300)

class TipoProd(models.Model):
    descripcion = models.TextField(max_length=255)

    def __str__(self):
        return self.descripcion

class Producto(models.Model):
    nombre = models.TextField(max_length=45)
    descripcion = models.TextField(max_length=255)
    idTipoProd = models.ForeignKey(TipoProd,on_delete=models.CASCADE)
    imagen = models.FileField(upload_to=user_directory_path)

class RegistroProd(models.Model):
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    visto = models.BooleanField()
    fecha = models.DateField()