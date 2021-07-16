from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    name = models.CharField(max_length=64)
    date = models.DateField(auto_now=True)


class Paper(models.Model):
    Category = models.TextChoices('Category', 'Semester Sessional-I Sessional-II')
    subject = models.CharField(max_length=64)
    year = models.IntegerField(default=2021)
    category = models.CharField(choices=Category.choices, max_length=12)
