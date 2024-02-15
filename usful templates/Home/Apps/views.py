from django.shortcuts import render,redirect
from . models import details
# Create your views here.

def index(request):
    fd = details.objects.all()
    return render(request,'index.html',{'fd':fd})

def navbar(request):
    return render(request,'navbar.html')
def booku(request):
    return render(request,'booking.html')
def booking(request):
    x= request.POST['food']
    y= request.POST['price']
    foods=details(food=x,price=y)
    foods.save()
    return redirect('booku')

from django.shortcuts import render, redirect
from .models import Person, Marks

def enter_info(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        person = Person.objects.create(name=name, age=age)
        return redirect('enter_marks')
    return render(request, 'enter_info.html')

def enter_marks(request):
    persons = Person.objects.all()
    if request.method == 'POST':
        person_id = request.POST['name']
        marks = request.POST['marks']
        marks_entry = Marks.objects.create(person_id=person_id, marks=marks)
        return redirect('enter_marks')
    return render(request, 'enter_marks.html', {'persons': persons})

def get_marks(request):
    if request.method == 'POST':
        person_id = request.POST['name']
        marks = Marks.objects.filter(person_id=person_id)
        return render(request, 'display_marks.html', {'marks': marks})
    return redirect('')

