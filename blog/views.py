from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .forms import UserForm


def usuario_list(request):
    return render(request, 'blog/usuario_list.html', {})

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def create(request):
    
    form =UserForm()
    return render(request,'create.html',{'form': form})