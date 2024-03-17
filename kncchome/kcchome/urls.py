from django.urls import path
from . import views

urlpatterns=[
    path('', views.home,name='home'),
    path('union/', views.unions,name='unions'),
    path('galary/', views.gallery,name='us'),


]