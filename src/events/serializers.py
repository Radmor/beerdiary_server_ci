from rest_framework import serializers
from pubs.serializers import PubSerializer

from .models import Event
from pubs.models import Pub

class EventSerializer(serializers.ModelSerializer):
    place = serializers.PrimaryKeyRelatedField(queryset=Pub.objects.all())
    class Meta:
        model = Event
        fields = ('name', 'start_date', 'end_date', 'description','place')