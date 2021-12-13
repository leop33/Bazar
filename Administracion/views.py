from django.shortcuts import render, redirect
from django.views import View
from django_tables2 import RequestConfig
from Administracion import tables
from Cliente import models
from Administracion import forms
# Create your views here.
per_page = 8

def table_productos(request):
    table = tables.ProductosTable(data=models.Producto.objects.all())
    RequestConfig(request).configure(table)
    table.paginate(page=request.GET.get("page", 1), per_page=per_page)
    return table

def table_clientes(request):
    table = tables.ClientesTable(data=models.RegistroProd.objects.all())
    RequestConfig(request).configure(table)
    table.paginate(page=request.GET.get("page", 1), per_page=per_page)
    return table

class Main(View):
    def get(self,request):
        context = {
            "title": "Administrador",
            "app_name": request.user,
            "user":request.user
        }
        return render(request, "Administracion/Main.html", context)

class AddProductoView(View):
    title = 'Productos'

    def get(self, request):
        form = forms.ProductosForm()
        return render(request, 'Administracion/Productos.html', {
            "title": self.title,
            "form": form,
            "table": table_productos(request),
        })

    def post(self, request):
        form = forms.ProductosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return render(request, 'Administracion/Productos.html', {
            "title": self.title,
            "form": form,
            "table": table_productos(request),
        })


class EditProductosView(View):
    title = 'Productos'

    def get(self, request, method, pk):
        try:
            producto = models.Producto.objects.get(pk=pk)
            form = forms.ProductosForm(instance=producto)
            return render(request, 'Administracion/Productos.html', {
                "title": self.title,
                "form": form,
                "active": pk,
                "table": table_productos(request),
                "method": method
            })
        except models.Producto.DoesNotExist:
            return redirect('AdminProducto')

    def post(self, request, method, pk):
        form = None
        try:
            producto = models.Producto.objects.get(pk=pk)
            if method == 'update':
                form = forms.ProductosForm(request.POST, request.FILES, instance=producto)
                if form.is_valid():
                    form.save()
                else:
                    print(form.errors)
            elif method == 'delete':
                producto.delete()
                form = forms.ProductosForm()
            return render(request, 'Administracion/Productos.html', {
                "title": self.title,
                "form": form,
                "active": pk,
                "table": table_productos(request),
            })
        except models.Producto.DoesNotExist:
            return redirect('AdminProducto')

class ClientesView(View):
    title = 'Clientes'

    def get(self, request):
        return render(request, 'Administracion/Clientes.html', {
            "title": self.title,
            "table": table_clientes(request),
        })