from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name= 'Id  Categoria')
    nombreCategoria =models.CharField(max_length=50, verbose_name= 'Nombre')
    def __str__(self):
        return self.nombreCategoria
#modelo para Libros
class Libro(models.Model):
    isbn = models.IntegerField(primary_key=True, verbose_name='Id Libro')
    nombre = models.CharField(max_length =40, verbose_name ='Nombre')
    autor = models.CharField(max_length =40, verbose_name ='Autor')
    descripcion =models.CharField(max_length =150, verbose_name ='Descripción')
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE)

    def __str__(self):
        return self.nombre