from django.db import models
# Create your models here.
def user_directory_path(instance, filename):
    print(f'{filename} guardado')
    if type(instance) == Producto:
        return f'static/Producto/{instance.nombre}.jpg'.strip().replace(" ","_")

class Cliente(models.Model):
    nombre = models.CharField(max_length=45)
    apellido1 = models.CharField(max_length=45)
    apellido2 = models.CharField(max_length=45)
    email = models.EmailField()
    telefono = models.CharField(max_length=10)
    mensaje = models.TextField(max_length=300)

    def __str__(self):
        nomcom=self.nombre+" "+self.apellido1+": "+self.mensaje+" Telefono y correo: "+self.telefono+" "+self.email
        return nomcom

class TipoProd(models.Model):
    descripcion = models.TextField(max_length=255)

    def __str__(self):
        return self.descripcion

class Producto(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.TextField(max_length=255)
    idTipoProd = models.ForeignKey(TipoProd,on_delete=models.CASCADE)
    imagen = models.FileField(upload_to=user_directory_path)

    def __str__(self):
        return self.nombre

class RegistroProd(models.Model):
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    visto = models.BooleanField(default=False)
    fecha = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('idCliente', 'idProducto')

    def __str__(self):
        return f'{self.fecha} / Producto'
