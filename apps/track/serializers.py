from rest_framework import serializers
from .models import Track
from apps.location.serializers import LocationSerializer


class TrackSerializer(serializers.ModelSerializer):
    current_location = LocationSerializer()

    class Meta:
        model = Track
        fields = '__all__'
