from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request,'index.html')

def register(request):
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')

def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.info(request,"user already exist")
            return render(request,'register.html')
        elif User.objects.filter(email=email).exists():
            messages.info(request,"email already taken")
            return render(request,'register.html')
        else:
          user=User.objects.create_user(username=username,email=email,password=password)
          user.save()
        return redirect('login')
    else:
     return render(request,'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request)
            if user.is_superuser:
                return redirect('index')
            elif user.is_staff:
                return redirect("index")
            else:
                return redirect("index")
        else:
            messages.info(request,"invalid login")
            return redirect('login')
    return redirect('login')