from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class AttendeeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Attendee
        fields = '__all__'
        
class EventSerializer(serializers.ModelSerializer):
    attendees = AttendeeSerializer(many=True, read_only=True)
    class Meta:
        model = Event
        fields = '__all__'
        
class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = '__all__'