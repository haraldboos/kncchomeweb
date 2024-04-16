from django.shortcuts import render
from django.db.models import Count
from django.db.models.functions import  ExtractMonth,ExtractYear
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
def alevents(request):
    # nev=nevbar.objects.filter(status=True).order_by('order')
  
    events = event.objects.filter(status=True).order_by('-eventdate')
    alleventsbydm = event.objects.annotate(year=ExtractYear('eventdate'),month=ExtractMonth('eventdate')).values('year','month').annotate(total=Count('eventid')).order_by('year','month')
    d_year = event.objects.values_list('eventdate__year',flat=True).distinct().order_by('eventdate__year')
    pornhub={}
    for year in d_year:
        pornhub[d_year] = event.objects.filter(eventdate__year=year).values_list('eventdate__month',flat=True).distinct().order_by('eventdate__month')
    print(alleventsbydm)
    print(events)
    print(nev)
    return render(request,'knctem/events.html',{'nev':nev,'fk':'fk','event':events})