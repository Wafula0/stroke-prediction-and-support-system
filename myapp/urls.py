from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('register_ordinary_user',views.register_ordinary_user,name='register_ordinary_user'),
    path('login_ordinary_user',views.login_ordinary_user,name='login_ordinary_user'),
    path('register_doctor',views.register_doctor,name='register_doctor'),
    path('login_doctor',views.login_doctor,name='login_doctor'),
    path('ordinary_user_hpage',views.ordinary_user_hpage,name='ordinary_user_hpage'),
    path('doctor_hpage',views.doctor_hpage,name='doctor_hpage'),
    path('logout',views.logout,name='logout'),
]
    