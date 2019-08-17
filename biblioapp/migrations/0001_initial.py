# Generated by Django 2.2.4 on 2019-08-17 02:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('descripción', models.TextField(max_length=40)),
                ('isbn', models.CharField(max_length=20)),
                ('cantidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaprestamo', models.DateField(verbose_name='Fecha de prestamo')),
                ('nombrecliente', models.CharField(max_length=50, verbose_name='Nombre del cliente')),
                ('telefonocliente', models.CharField(max_length=20, verbose_name='Telefono cliente')),
                ('estado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Ejemplar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroejemplar', models.CharField(max_length=30, verbose_name='Número de ejemplar')),
                ('fechacompra', models.DateField(verbose_name='Fecha de compra')),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioapp.Libro')),
            ],
        ),
        migrations.CreateModel(
            name='DetallePrestamo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ejemplar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioapp.Ejemplar')),
                ('prestamo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioapp.Prestamo')),
            ],
        ),
    ]
