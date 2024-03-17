from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import *
def home(request):
    nev=nevbar.objects.filter(status=True).order_by('order')
    print(nev)
    return render(request,'knctem/home.html',{'nev':nev})
def unions(request):
    nev=nevbar.objects.filter(status=True).order_by('order')
    print(nev)
    return render(request,'knctem/union.html')
def gallery(request):
    nev=nevbar.objects.filter(status=True).order_by('order')
    print(nev)
    return render(request,'knctem/gallery.html')

