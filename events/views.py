from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Event, EventImage, EventRSVP
from .serializers import EventSerializer, EventImageSerializer, EventRSVPSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.AllowAny] #Todo: remove when auth is working

class EventImageViewSet(viewsets.ModelViewSet):
    queryset = EventImage.objects.all().order_by("id")
    serializer_class = EventImageSerializer
    permission_classes = [permissions.AllowAny] #todo: remove when auth is working

    @action(detail=True, methods=['get'], url_path="images")
    def get_event_images(self, request, pk=None):
        images = EventImage.objects.filter(event_id=pk)
        serializer = EventImageSerializer(images, many=True, context={"request":request})
        return Response(serializer.data)
    
class EventRSVPViewSet(viewsets.ModelViewSet):
    queryset = EventRSVP.objects.all()
    serializer_class = EventRSVPSerializer
    permission_classes = [permissions.AllowAny]