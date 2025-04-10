from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()



class Event(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField()
    time = models.DateTimeField()
    location = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')



class Participant(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    event = models.ManyToManyField(Event, related_name='event')


