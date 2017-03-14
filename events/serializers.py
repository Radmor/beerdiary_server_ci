from rest_framework import serializers

from .models import Event

class EventSerializer(serializers.ModelSerializer):
    place = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Event
        fields = ('name', 'start_date', 'end_date', 'description','place')