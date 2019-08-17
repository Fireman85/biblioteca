from django.db import models
from django.urls import reverse

class Libro(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.TextField(max_length=40)
    isbn = models.CharField(max_length=20)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('detalle_libro', args=[str(self.id) ])

class Prestamo(models.Model):
    fechaprestamo = models.DateField("Fecha de prestamo")
    nombrecliente = models.CharField("Nombre del cliente",max_length=50)
    telefonocliente = models.CharField("Telefono cliente",max_length=20)
    estado = models.BooleanField(default= False)

    def __str__(self):
        return self.fechaprestamo.strftime('%d/%m/%Y')

class Ejemplar(models.Model):
    numeroejemplar = models.CharField("Número de ejemplar", max_length=30)
    fechacompra =models.DateField("Fecha de compra")
    libro = models.ForeignKey('Libro', on_delete = models.CASCADE)

    def __str__(self):
        return "{}-{}".format(self.libro, self.numeroejemplar)

class DetallePrestamo(models.Model):
    prestamo = models.ForeignKey('Prestamo', on_delete=models.CASCADE)
    ejemplar = models.ForeignKey('Ejemplar', on_delete=models.CASCADE)

    def __str__(self):
        return "{}-{}".format(self.prestamo, self.ejemplar)



