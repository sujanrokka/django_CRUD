from django.db import models
from ckeditor.fields import RichTextField


class Student(models.Model):
    name=models.CharField(max_length=60)
    roll=models.IntegerField()
    # city=models.CharField(max_length=50)
    city = RichTextField(blank= True, null = True)
    
