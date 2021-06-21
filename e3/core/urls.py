from django.urls import path 
from .views import home, form_libro , registro_persona , form_modificar_libro

urlpatterns =[
    path('',home,name="home"),
    path('form-libro',form_libro, name='form_libro'),
    path('registro-persona',registro_persona,name="registro_persona"),
    path('form-modificar-libro/<id>',form_modificar_libro,name="form_modificar_libro"),
]