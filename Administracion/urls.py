from django.contrib.auth.decorators import login_required
from django.urls import path
from django.contrib.auth import views as admin_views
from . import views

urlpatterns = [
    path('Login/', admin_views.LoginView.as_view(), {
        'template_name': 'login.html', 'app_name': 'Login'
    }, name='login'),
    path('Logout/', admin_views.logout_then_login, name = 'logout'),

    path('', login_required(views.Main.as_view()), name = 'index'),

    path('adminProd/', login_required(views.VProducto.as_view()), name = 'VProducto'),

]