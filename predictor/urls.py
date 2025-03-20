from django.urls import path
from . import views

urlpatterns=[
    path('predict',views.predict,name='predict'),
    path('results',views.results,name='results')
]