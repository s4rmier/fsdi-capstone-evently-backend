from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=28)
    description = models.TextField(max_length=256)
    address = models.CharField(max_length=64)
    time = models.TimeField(default='00:00') 
    date = models.DateField() 

    def __str__(self):
        return self.title
    
class EventImage(models.Model):
    event = models.ForeignKey(Event, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="event_images/")