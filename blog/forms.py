from django import forms
from django.forms import ModelForm
from .models import Usuario

#Creo un formulario para los usuarios
class UserForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ('nombre','apellido','correo')
        labels = {
            'nombre': '',
            'apellido': '',
            'correo': '',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}),
            'apellido': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido'}),
            'correo':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Correo'}),
        }