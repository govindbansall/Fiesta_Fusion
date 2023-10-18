from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.name
    
class Venue(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    capacity = models.IntegerField(default=50)
    
    def __str__(self):
        return self.name
    # Add any additional fields you'd like for the Venue model

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    capacity = models.IntegerField(default=50)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events_created')
    # Add any additional fields you'd like for the Event model
    
    def __str__(self):
        return self.title
    
class Attendee(models.Model):
    event = models.ForeignKey(Event, related_name='attendees', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='attendees', on_delete=models.CASCADE)