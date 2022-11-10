from django.urls import path
from . import views

urlpatterns = [
    path('', views.agregarUsuario, name='agregarUsuario'),
    path('agregarUsuario', views.agregarUsuario, name='agregarUsuario'),
    path('agregarUsuario.html', views.agregarUsuario, name='agregarUsuario'),
    path('table.html', views.crearTabla, name='crearTabla'),
]