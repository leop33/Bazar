# Generated by Django 3.2.9 on 2021-12-13 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0002_auto_20211213_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='apellido1',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='apellido2',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='mensaje',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombre',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=45),
        ),
    ]
