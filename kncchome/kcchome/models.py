from django.db import models
import datetime
import os
# Create your models here.
def uploadpro(request,filename):
        curtime=datetime.datetime.now().strftime("%Y%m%d:%H%M%S")
        filenewname=curtime+filename
        return os.path.join('img/',filenewname)
class  nevbar(models.Model):
    nevbrtext= models.CharField(max_length=20,primary_key=True)
    status = models.BooleanField(default=True,help_text='1-for show 0 for not show')
    order = models.IntegerField(default=None)

    def __str__(self):
        return self.nevbrtext

class nevdrop(models.Model):
    nevbar = models.ForeignKey(nevbar, on_delete=models.CASCADE)
    name = models.CharField(max_length=15,blank=False,default=None)
    status = models.BooleanField(default=True,help_text='1-for show 0 for not show')
    # order = models.IntegerField(default=None)


    def __str__(self):
        return self.name
class achivet(models.Model):
    date = models.DateField(default=None)
    title=models.CharField(max_length=16,blank=False,default=None)
    status = models.BooleanField(default=True,help_text='1-for show 0 for not show')
    textdesc = models.CharField(max_length=50,blank=False,default=None)
    images = models.ImageField(upload_to=uploadpro,blank=True,verbose_name="Upload image for home achivements")

    def __str__(self):
        return self.title
    
class news(models.Model):
    newsid = models.AutoField(primary_key=True,default=None) 
    newshd=models.CharField(default=None,max_length=30,verbose_name="Head lines of News")
    newsdetails = models.CharField(default=None,max_length=70,verbose_name="Details about News")
    newsdate = models.DateField(default=None,verbose_name="enter the news date")
    status = models.BooleanField(default=True,help_text='1-for show 0 for not show')

    def __str__(self):
        return str(self.newsid)
    
class achivement(models.Model):
    aid = models.AutoField(primary_key=True,default=None) 

    aimage = models.ImageField(upload_to=uploadpro,null=False,blank=False,verbose_name="upload a photo of achievment")
    atitle = models.CharField(default=None,max_length=30,verbose_name="Enter the heading of achievment")
    adetail = models.CharField(default=None,max_length=60,verbose_name="Enter the detailo  of achievment")
    adate = models.DateField(default=None,verbose_name="enter the news date")
    status = models.BooleanField(default=True,help_text='1-for show 0 for not show')


class page(models.Model):
    pass

class event(models.Model):
    eventid = models.AutoField(primary_key=True,default=None) 

    eventu = models.ForeignKey(nevdrop,on_delete=models.CASCADE)
    coverimg = models.ImageField(upload_to=uploadpro,null=False,blank=False,verbose_name="upload a photo of event")
    eventdate =models.DateField(default=None,verbose_name="enter the Event data")
    status = models.BooleanField(default=True,help_text='1-for show 0 for not show')
    eventitle = models.CharField(default=None,max_length=30,verbose_name="Enter the heading of event")
    eventdisc = models.CharField(default=None,max_length=360,verbose_name="Enter the detailo  of event")
    homeshow = models.BooleanField(default=False,help_text='1-for show 0 for not show',verbose_name="show the card in home")


    def __str__(self):
        return str(self.eventid)
class eventalbum(models.Model):
    event= models.ForeignKey(event,on_delete=models.CASCADE)
    imag= models.ImageField(upload_to=uploadpro,null=False,blank=False,verbose_name="upload a photo of event")
    status = models.BooleanField(default=True,help_text='1-for show 0 for not show')

    eventaldate =models.DateField(default=None,verbose_name="enter the Event date")

    
class history(models.Model):
    status = models.BooleanField(default=True,help_text='1-for show 0 for not show')
    histdate =models.DateField(default=None,verbose_name="enter the Event date")
    histdetail = models.CharField(default=None,max_length=160,verbose_name="Enter the detailo  of event")


