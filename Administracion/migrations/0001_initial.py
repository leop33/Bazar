# Generated by Django 3.2.9 on 2021-11-25 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoProd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nick', models.CharField(max_length=45, unique=True)),
                ('nombre', models.TextField()),
                ('apellido1', models.TextField()),
                ('apellido2', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(max_length=255)),
                ('nombre', models.TextField(max_length=45)),
                ('imagen', models.TextField(max_length=45)),
                ('idTipoProd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Administracion.tipoprod')),
            ],
        ),
    ]