from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
#from.models import Feature

 #Create your views here.

def index(request):
    return render(request, 'landing.html')

def ordinary_user_hpage(request):
    return render(request, 'ordinaryuserhome.html')

def doctor_hpage(request):
    return render(request, 'healthofficerhome.html')




def register_ordinary_user(request):
    
    if request.method =='POST':
        username=request.POST['username']
        email=request.POST['email']
        country=request.POST['country']
        password=request.POST['password']
        password2=request.POST['password2']


        if password==password2:
            if User.objects.filter(email=email).exists():
               messages.info(request, 'Email Already Used')
               return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists!')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.country=country
                user.save()
                return redirect('login_ordinary_user')
        else:
            messages.info(request, "password Not the same")
            return redirect('register_ordinary_user')
    else:
        return render(request,'register_ordinary_user.html')


        

     
    return render(request,'register.html')

def login_ordinary_user(request):
    if request.method=='POST':
        password=request.POST['password']
        username=request.POST['username']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('ordinary_user_hpage')
        else:
            messages.info(request,'credentials invalid!')
            return redirect('login_ordinary_user')

    else:
        return render(request,'login_ordinary_user.html')


def register_doctor(request):
    
    if request.method =='POST':
        username=request.POST['username']
        email=request.POST['email']
        country=request.POST['country']
        licensenumber=request.POST['licensenumber']
        password=request.POST['password']
        password2=request.POST['password2']


        if password==password2:
            if User.objects.filter(email=email).exists():
               messages.info(request, 'Email Already Used')
               return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists!')
                return redirect('register')
            else:
                myuser=User.objects.create_user(username=username,email=email,password=password)
                myuser.country=country
                myuser.licensenumber=licensenumber
                myuser.save()
                return redirect('login_doctor')
        else:
            messages.info(request, "password Not the same")
            return redirect('register')
    else:
        return render(request,'register_doctor.html')


        

     
    return render(request,'register.html')

def login_doctor(request):
    if request.method=='POST':
        password=request.POST['password']
        username=request.POST['username']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('doctor_hpage')
        else:
            messages.info(request,'credentials invalid!')
            return redirect('login_doctor')

    else:
        return render(request,'login_doctor.html')


    #return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

