from django.shortcuts import render, redirect
from django.template import loader
from .models import Libro
from .forms import LibroForm

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def lista(request):
    libros = Libro.objects.all()
    datos={
        'libros': libros
    }
    return render(request, 'core/lista.html',datos)

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
            
    return render (request, 'core/form_libro.html', datos)

def form_modificar_libro(request, id):
    libro = Libro.objects.get(isbn=id)
    datos= {
        'form': LibroForm(instance=libro)
    }
    if request.method =='POST':
        formulario = LibroForm(data=request.POST, instance=Libro)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje']= "Modificado exitosamente"
     
    return render(request, 'core/form_modificar_libro.html',datos)


def form_del_libro(request, id):
    libro = Libro.objects.get(isbn=id)
    libro.delete()
    return  redirect(to="lista")
    
  
