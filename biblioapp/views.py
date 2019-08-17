from django.shortcuts import render
from .models import Libro

from .forms import LibroForm

from django.views.generic.edit import CreateView


def iniciar(request):
    return render(request,'biblioapp/index.html')


def muestralibros(request):
    form = LibroForm()
    todosloslibros = Libro.objects.all()
    return render(request,'biblioapp/libros.html', {'libros': todosloslibros, 'form': form, })


def detallelibro(request, id):
    libro = Libro.objects.get(pk = id)
    return render(request,'biblioapp/detallelibro.html', {'libro': libro})


class NuevoLibro(CreateView):
    model = Libro
    fields = ['nombre','descripcion','isbn','cantidad']
    #template_name = 'biblioapp/libros.html'
    #form_class = LibroForm


