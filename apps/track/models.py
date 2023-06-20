from django.db import models
from apps.location.models import Location


class Track(models.Model):
    unique_number = models.CharField(max_length=5)
    current_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    carrying_capacity = models.PositiveIntegerField()
