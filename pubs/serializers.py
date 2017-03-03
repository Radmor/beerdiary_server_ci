from rest_framework import serializers
from .models import Pub


class PubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pub
        fields = ('name', 'street', 'city', 'overall', 'design', 'design_description', 'atmosphere', 'atmosphere_description',)
