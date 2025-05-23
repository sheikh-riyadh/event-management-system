from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="category name", unique=True)
    category_description = models.TextField(verbose_name="category description")

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=50, verbose_name="event name", unique=True)
    description = models.TextField(verbose_name="event description")
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='events')

    def __str__(self):
        return self.title


class Participant(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    events = models.ManyToManyField(Event, related_name='participants')

    def __str__(self):
        return self.name
