from django.shortcuts import render
from django.views import View
from Administracion.models import Producto
# Create your views here.
class VProducto(View):
    def get(self, request):
        context = {
            "app name": f'Administracion | Productos',
            "user": request.user,
            "prod": Producto.objects.all(),
        }
        return render(request, 'VProducto.html',context)

class Main(View):
    def get(self,request):
        context = {
            "title": "Administrador",
            "app_name": "Administrador | Main",
            "user":request.user
        }
        return render(request,"Main.html",context)