from django.urls import path 
from .views import home, form_libro , registro_persona , form_modificar_libro,lista, form_del_libro

urlpatterns =[
    path('',home,name="home"),
    path('lista',lista,name="lista"),
    path('form-libro',form_libro, name='form_libro'),
    path('registro-persona',registro_persona,name="registro_persona"),
    path('form-modificar-libro/<id>',form_modificar_libro,name="form_modificar_libro"),
    path('form-del-libro/<id>',form_del_libro,name="form_del_libro"),
]