from django.urls import path, include
from .views import uservs, venuevs, eventvs, attendeevs
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', uservs)
router.register(r'venues', venuevs)
router.register(r'events', eventvs)
router.register(r'attendees',attendeevs)

urlpatterns = [
    path('',include(router.urls)),
]