from django.contrib.auth.decorators import login_required
from django.urls import path
from django.contrib.auth import views as admin_views
from . import views

urlpatterns = [
    path('Login/', admin_views.LoginView.as_view(), {'template_name': 'login.html'}, name='login'),
    path('Logout/', admin_views.logout_then_login, name = 'logout'),
    path('Main/', login_required(views.Main.as_view()), name = 'MainAdmin'),
    path('Producto/', login_required(views.AddProductoView.as_view()), name = 'AdminProducto'),
    path('Producto/<method>/<pk>', login_required(views.EditProductosView.as_view())),
    path('Clientes/',  login_required(views.ClientesView.as_view()), name="AdminClientes"),
]