from django import forms
from .models import Libro

class LibroForm(forms.Form):
    nombre = forms.CharField(max_length=35)
    descripcion = forms.CharField(widget=forms.Textarea,max_length=35)
    isbn = forms.CharField(max_length=35)
    cantidad = forms.IntegerField()

    class Meta:
        model = Libro