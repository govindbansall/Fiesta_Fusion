from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from .serializers import *
from .models import *

# Create your views here.

 
    
class uservs(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
        
class venuevs(viewsets.ModelViewSet):
    queryset=Venue.objects.all()
    serializer_class=VenueSerializer
    #for event search and filtering
    filter_backends = [SearchFilter]
    search_fields = ['id', 'location', 'name']
    
class eventvs(viewsets.ModelViewSet):
    queryset=Event.objects.all()
    serializer_class=EventSerializer
    
    
    def create(self, request, *args, **kwargs):
        event_data = request.data
        event_capacity = event_data.get('capacity')
        attendee_count = Attendee.objects.filter(event=event_data.get('id')).count()
        if attendee_count>=event_capacity:
            return Response({'error':'event is already full'},status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)
    
class attendeevs(viewsets.ModelViewSet):
    queryset=Attendee.objects.all()
    serializer_class=AttendeeSerializer