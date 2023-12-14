from django.contrib import admin
from .models import Event, EventImage, EventRSVP

# Register your models here.
admin.site.register(Event)
admin.site.register(EventImage)
admin.site.register(EventRSVP)

