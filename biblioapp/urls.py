from django.urls import path

from .views import iniciar, muestralibros, detallelibro, NuevoLibro

urlpatterns = [
    path('', iniciar, name = 'inicio'),
    path('libros/', muestralibros, name = 'muestra_libros'),
    path('libros/<int:id>/', detallelibro, name = 'detalle_libro'),
    path('libros/nuevo/', NuevoLibro.as_view(), name = 'nuevo_libro'),
]