from django.contrib.auth.models import User
from django.db import models


class Trip(models.Model):
    added_time = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)
    arrival_time = models.DateTimeField()
    return_time = models.DateTimeField()
    # Destination
    address = models.CharField(max_length=500)
    # price = models.IntegerField()
    # current_address = models.CharField(max_length=500)
    # details for the flight
    record_locator = models.CharField(max_length=500, blank=True)
