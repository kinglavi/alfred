from django.db import models


class Trip(models.Model):
  arriavel_time = models.DateTimeField()
  return_time = models.DateTimeField()
  long_position = models.DecimalField(max_digits=8, decimal_places=3)
  lat_position = models.DecimalField(max_digits=8, decimal_places=3)
