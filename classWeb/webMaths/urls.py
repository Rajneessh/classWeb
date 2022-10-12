from django.contrib import admin
from django.urls import path,include
from . import views 

urlpatterns = [
    path('', views.maths, name='maths'),
    path('add/',views.add, name='add'),
    path('sub/',views.sub, name='sub'),
    path('addResult/',views.addResult, name='addResult'),
    path('subResult/',views.subResult, name='subResult'),
]
