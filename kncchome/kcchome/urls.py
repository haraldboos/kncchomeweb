from django.urls import path
from . import views

urlpatterns=[
    path('', views.home,name='home'),
    path('union/<str:union>', views.unions,name='unions'),
    path('galary/<int:event>', views.gallery,name='galary'),
    path('history/', views.histoory,name='history'),
    path('sgallery/', views.sgallery,name='sgalary'),
    path('events/', views.alevents,name='event'),

    path('oba/',views.oba,name='oba')

]