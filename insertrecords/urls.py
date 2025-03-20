from django.urls import path
from . import views

urlpatterns =[
    path('insertRecords', views.insertRecords,name = 'insertRecords'),
    
]