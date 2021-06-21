from django.shortcuts import render, redirect
from django.template import loader
from .models import Libro
from .forms import LibroForm

# Create your views here.
def home(request):
    return render(request, 'core/home.html')


def registro_persona(request):
    return render(request, 'core/registro_persona.html')

def form_libro(request):
    datos = {
        'form': LibroForm()
    }
    if request.method =='POST':
        formulario = LibroForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensje']= "Datos Guardados Exitosamente"
    return render (request, 'core/form_libro.html', dato)