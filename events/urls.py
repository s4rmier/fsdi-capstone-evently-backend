from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, EventImageViewSet

router = DefaultRouter()
router.register('event', EventViewSet, basename='event')
router.register('eventImage', EventImageViewSet, basename='eventImage')

urlpatterns = router.urls
urlpatterns += []