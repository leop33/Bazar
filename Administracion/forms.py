from django import forms
from django.forms import ModelForm
import Administracion.models as models

class ProductoForm(ModelForm):
    tipo = forms.ModelChoiceField(queryset = models.TipoProd.objects.all())

    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)

    class Meta:
        model= models.Producto
        fields = ['descripcion', 'nombre', 'imagen', 'tipo']

        widgets = {
            'descripcion': forms.TextInput(), 'nombre': forms.TextInput(),
            'imagen': forms.TextInput()
        }


