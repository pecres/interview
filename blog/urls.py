from django.urls import path
from . import views

urlpatterns = [
    path('', views.agregarUsuario, name='agregarUsuario'),
    path('agregarUsuario', views.agregarUsuario, name='agregarUsuario'),
    path('tabla', views.crearTabla, name='crearTabla'),
]