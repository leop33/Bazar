# Generated by Django 3.2.9 on 2021-12-13 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0004_alter_cliente_mensaje'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(max_length=255),
        ),
    ]