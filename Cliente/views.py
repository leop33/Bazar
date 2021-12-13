import json
import os

from django.conf import settings
from django.forms.utils import ErrorDict
from django.shortcuts import render
from django.views import View

from Cliente.forms import InteresadoForm
from Cliente import models as m
from django.shortcuts import render

class MainView(View):
    title = 'Main'

    def get(self, request):

        if settings.DEBUG:
            for i in m.Producto.objects.all():
                i.imagen = f'static/Producto/{i.nombre}.jpg'
                i.save()

        return render(request, 'Cliente/Main.html', {
            "title": self.title,
            "productos": m.Producto.objects.all().order_by('-id')[0:6],
        })


class NosotrosView(View):
    title = 'Nosotros'

    def get(self, request):

        return render(request, 'Cliente/Nosotros.html', {
            "title": self.title,
            "Somos": 'Somos Sakura Bazar :D',
            "Vision": 'Ser el mejor bazar',
            "Mision": 'Ser bien bien chidos',
            "Valores": 'Honestos y chidos'
        })
class ContactoView(View):
    title = 'Contacto'

    def get(self, request):

        return render(request, 'Cliente/Contacto.html', {
            "title": self.title,
            "Correos": 'sakurabazar@gmail.com',
            "Telefonos": '4433546436',
        })
class ProductosView(View):
    title = "Productos"

    def get(self, request, tipo=None):
        return render(request, 'Cliente/Productos.html', {
            "title": self.title,
            "productos": m.Producto.objects.all().order_by('-id'),
            "tipos": m.TipoProd.objects.all(),
        })


class ProductoView(View):
    title = "Producto"

    def get(self, request, pk):
        return render(request, 'Cliente/Producto.html', {
            "title": self.title,
            "item": m.Producto.objects.get(pk=pk)
        })
class InteresadoView(View):
    title = "Interesado"

    def get(self, request,  pk):
        item = m.Producto.objects.get(pk=pk)

        form = InteresadoForm()
        return render(request, 'Cliente/Interesado.html', {
            "title": self.title,
            "item": item,
            "form": form,
        })

    def post(self, request, pk):
        item = None
        form = InteresadoForm(request.POST)
        status = form.is_valid()
        if status:
            new_cliente = form.save()
            item = m.Producto.objects.get(pk=pk)
            new_interesado_producto = m.RegistroProd(
                idCliente=new_cliente,
                idProducto=item
            )
            new_interesado_producto.save()
            print(request.method == 'POST')
            return render(request, 'Cliente/%s.html' % ('Producto'), {
                "title": self.title,
                "item": item,
                "success": status,
            })
        else:
                item = m.Producto.objects.get(pk=pk)
        return render(request, 'Cliente/Interesado.html', {
            "title": self.title,
            "item": item,
            "form": form,
            "success": status,
            "msgs": form.errors.as_data()
        })
# Create your views here.
