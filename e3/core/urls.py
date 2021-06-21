from django.urls import path 
from .views import home, form_libro , registro_persona

urlpatterns =[
    path('',home,name="home"),
    path('form-libro',form_libro, name='form_libro'),
    path('registro-persona',registro_persona,name="registro_persona"),
]