from django.db import models

# Create your models here.
class  nevbar(models.Model):
    nevbrtext= models.CharField(max_length=10,primary_key=True)
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

class page(models.Model):
    pass