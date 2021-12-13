from django import forms

from Cliente import models


class InteresadoForm(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = "__all__"