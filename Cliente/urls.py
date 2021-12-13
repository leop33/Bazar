from django.urls import path
from . import views

urlpatterns = [
    path('Main/', views.MainView.as_view(), name="Main_client"),
    path('Contacto/', views.ContactoView.as_view(), name="Contacto"),
    path('Nosotros/', views.NosotrosView.as_view(), name="Nosotros"),
    path('Productos/', views.ProductosView.as_view(), name="Productos"),
    path('Productos/<tipo>', views.ProductosView.as_view(), name="Productos_filtro"),
    path('Producto/<pk>', views.ProductoView.as_view(), name="Producto"),
    path('Interesado/<pk>', views.InteresadoView.as_view(), name="Interesado"),
]