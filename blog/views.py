from django.shortcuts import render
from .forms import UserForm
from django.shortcuts import redirect
from .models import Usuario
from django.template import loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect

def agregarUsuario(request):
  registrado = False
  if request.method =="POST":
    form = UserForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('agregarUsuario?registrado=True')
  else:
    form = UserForm
    if 'registrado' in request.GET:
      registrado = True
  return render(request, 'agregarUsuario.html',{'form':form, "registrado":registrado})

#necesito incluir la tabla en agregarUsuario
def crearTabla(request):
  query = Usuario.objects.all()
  template = loader.get_template('table.html')
  context = {'myusers': query}
  
  return HttpResponse(template.render(context, request))