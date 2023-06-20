from rest_framework import serializers
from .models import Cargo
from apps.location.serializers import LocationSerializer


class CargoSerializer(serializers.ModelSerializer):
    pick_up = serializers.CharField()
    delivery = serializers.CharField()

    class Meta:
        model = Cargo
        fields = '__all__'
