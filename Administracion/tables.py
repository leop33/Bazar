from django.utils.html import format_html

from Cliente import models
import django_tables2 as tables


class ImageColumnP(tables.Column):
    def render(self, value):
        return format_html('<img src="/{}" alt="/{}" />', value, value)


class ProductosTable(tables.Table):
    imagen = ImageColumnP()

    class Meta:
        model = models.Producto
        exclude = ("id",)
        row_attrs = {
            "row-id": lambda record: record.pk
        }