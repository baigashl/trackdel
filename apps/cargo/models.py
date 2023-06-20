from django.db import models
from apps.location.models import Location


class Cargo(models.Model):
    pick_up = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='pick_up_cargos')
    delivery = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='delivery_cargos')
    weight = models.PositiveIntegerField()
    description = models.TextField()

