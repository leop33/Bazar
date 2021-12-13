from django import forms

from Cliente import models

class ProductosForm(forms.ModelForm):
    class Meta:
        model = models.Producto
        fields = "__all__"
        widgets = {
            "descripcion": forms.Textarea(attrs={'rows': 3}),
        }


