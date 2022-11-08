from django import forms

class UserForm(forms.Form):

    nombre = forms.CharField(max_length=200, min_length=3, required=True)
    apellido = forms.CharField(max_length=200, min_length=3, required=True, widget=forms.Textarea(attrs={'row':5,'cols':3}))
    correo = forms.CharField(max_length=200)