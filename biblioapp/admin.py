from django.contrib import admin

from .models import Prestamo, DetallePrestamo, Libro, Ejemplar

admin.site.register(Prestamo)
admin.site.register(DetallePrestamo)
admin.site.register(Libro)
admin.site.register(Ejemplar)
