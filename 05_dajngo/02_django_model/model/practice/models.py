from turtle import update
from venv import create
from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    major = models.CharField(max_length=100)
    is_married = models.BooleanField(default=False)

    def __str__(self):
        return f'<{self.pk}: {self.name}>'

class Article(models.Model):
    title = models.CharField(max_length=200)
    context = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_married = models.BooleanField(default=False)
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    
    
    def __str__(self):
        return f'{self.pk}: {self.title}'




    
