from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

# Create your models here.
class UsuarioManager(BaseUserManager):
    def create_superuser(self, username, name, apellido1, apellido2, password):
        if not username:
            raise ValueError('No hay username')
        usuario = self.model(
            username=username,
            name=name,
            apellido1=apellido1,
            apellido2=apellido2
        )
        usuario.set_password(password)
        usuario.save()
        return usuario

class Usuario(AbstractBaseUser):
    username = models.CharField(max_length=45, unique=True)
    name = models.TextField(max_length=45)
    apellido1 = models.TextField(max_length=45)
    apellido2 = models.TextField(max_length=45)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = 'name', 'apellido1', 'apellido2'

    objects = UsuarioManager()

    def __str__(self):
        return f'{self.name.capitalize()} {self.apellido2.capitalize()} {self.apellido1.capitalize()}'