from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import *
nev=nevbar.objects.filter(status=True).order_by('order')

def home(request):
    # nev=nevbar.objects.filter(status=True).order_by('order')
    newss= news.objects.filter(status=True).order_by('-newsdate')[:4]
  
    achiv = event.objects.filter(status=True).filter(homeshow=True).order_by('-eventdate')
    print(achiv)
    # for newss in newss:
    #     print(newss.newshd)
    for achi in achiv:
        print(achi)
    return render(request,'knctem/home.html',{'nev':nev,'news':newss,'achev':achiv})
def unions(request,union):
    # nev=nevbar.objects.filter(status=True).order_by('order')
    events = event.objects.filter(status=True).filter(eventu__name=union).order_by('-eventdate')
    print(events)
    print(nev)
    return render(request,'knctem/union.html',{'nev':nev,'fk':'fk','event':events})
def gallery(request,event):
    # nev=nevbar.objects.filter(status=True).order_by('order')
    phto = eventalbum.objects.filter(status=True).filter(event__eventid=event)

    print(phto)
    return render(request,'knctem/gallery.html',{'nev':nev,'fk':'fk','photo':phto})
def histoory(request):
    histd = history.objects.filter(status=True).order_by('histdate')    # print(histd)
    return render(request,'knctem/histroy.html',{'nev':nev,'fk':'fk','hist':histd})

def oba(request):
    return render(request,'knctem/oba.html')

def sgallery(request):
    return render(request,'knctem/sgallery.html')