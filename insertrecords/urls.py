from django.urls import path
from . import views

urlpatterns =[
    path('insertRecords', views.insertRecords,name = 'insertRecords'),
    path('view_records',views.view_records,name='view_records'),
    
]