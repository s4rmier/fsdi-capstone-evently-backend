from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, EventImageViewSet, EventRSVPViewSet

router = DefaultRouter()
router.register('event', EventViewSet, basename='event')
router.register('eventImage', EventImageViewSet, basename='eventImage')
router.register('eventRSVP', EventRSVPViewSet, basename='eventRSVP')

urlpatterns = router.urls
urlpatterns += []