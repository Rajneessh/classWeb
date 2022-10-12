from django.contrib import admin
from django.urls import path,include
from classWork import views
urlpatterns = [
    path('', views.classHome,name='class'),
    path('timetable/', views.timeTable, name='time-table'),
    path('excel/',views.excel, name="excelProcessing"),
]
