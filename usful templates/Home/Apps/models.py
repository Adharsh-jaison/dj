from django.db import models

# Create your models here.

class details(models.Model):
    food = models.CharField(max_length=50)
    price = models.IntegerField(default=True)

# models.py

from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Marks(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    marks = models.DecimalField(max_digits=5, decimal_places=2)
