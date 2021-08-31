from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.enums import Choices
from django.db.models.fields import CharField


# Create your models here.
class Note(models.Model):
    subject = models.CharField(max_length=32, default='')
    title = models.CharField(max_length=64, default='')
    source = models.CharField(max_length=164, default='')
    your_name = models.CharField(max_length=64, default='')
    file_url = models.URLField(default='')
    date = models.DateField(auto_now_add=True)


class Paper(models.Model):    
    subject = models.CharField(max_length=32, default='')
    title = models.CharField(max_length=64, default='')
    uploader = models.CharField(max_length=64, default='')
    category = models.CharField(max_length=12, default='')
    year = models.IntegerField(default=2021)
    file_url = models.URLField(default='')


    