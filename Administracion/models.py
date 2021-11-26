from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

# Create your models here.
class TipoProd(models.Model):
    descripcion = models.TextField(max_length=255)

class Producto(models.Model):
    descripcion = models.TextField(max_length=255)
    nombre = models.TextField(max_length=45)
    imagen = models.TextField(max_length=45)
    idTipoProd = models.ForeignKey(TipoProd,on_delete=models.CASCADE)


class UsuarioManager(BaseUserManager):
    def create_superuser(self, nick, nombre, apellido1, apellido2, contrasena):
        usuario = self.model(
            nick=nick,
            nombre=nombre,
            apellido1=apellido1,
            apellido2=apellido2
        )
        usuario.set_password(contrasena)
        usuario.save()
        return usuario

class Usuario(AbstractBaseUser):
    nick = models.CharField(max_length=45, unique=True)
    nombre = models.TextField()
    apellido1 = models.TextField()
    apellido2 = models.TextField()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = 'nombre', 'apellido1', 'apellido2'

    objects = UsuarioManager()

    def __str__(self):
        return self.apellido1+' '+self.apellido2+' '+self.name