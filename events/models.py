from django.db import models

# Create your models here.
class Event(models.Model):
    eventTitle = models.CharField(max_length=28)
    eventDescription = models.TextField(max_length=256)
    eventAddress = models.CharField(max_length=64)
    eventTime = models.TimeField(default='00:00') 
    eventDate = models.DateField() 

    def __str__(self):
        return self.eventTitle
    
class EventImage(models.Model):
    event = models.ForeignKey(Event, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="event_images/")
    imgtype = models.IntegerField(blank=True, null=True)