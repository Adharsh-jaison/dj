from django.shortcuts import render,redirect
from . import views
from . models import Member
# Create your views here.

def home(request):
    mem = Member.objects.all()
    count = Member.objects.all().count()
    return render(request,'home_todo.html',{'mem':mem,'count':count})

def dummy(request):
    mem = Member.objects.all()
    return render(request,'dummy.html',{'mem':mem})

def add(request):
    return render(request,'add.html')

def addrec(request):
    x= request.POST['first']
    y= request.POST['last']
    z= request.POST['country']
    mem=Member(firstname=x,lastname=y,country=z)
    mem.save()
    return redirect('/')

def delete(request,id):
    mem=Member.objects.get(id=id)
    mem.delete()
    return redirect('/')

def update(request,id):
    mem=Member.objects.get(id=id)
    return render(request,'update.html',{'mem':mem})

def uprec(request,id):
    x= request.POST['first']
    y= request.POST['last']
    z= request.POST['country']
    mem=Member.objects.get(id=id)
    mem.firstname=x
    mem.lastname=y
    mem.country=z

    mem.save()
    return redirect('/')