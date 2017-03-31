from django.db import models

from alfredo_api.Trip.model import Trip


class OrderFlight(models.Model):
    trip = models.ForeignKey(Trip)
    origin = models.CharField(max_length=500)
    destination = models.CharField(max_length=500)
    departure_datetime = models.DateTimeField()
    arrival_date = models.DateTimeField()
    arrival_time = models.DateTimeField()
    air_line_name = models.CharField(max_length=500)
    flight_number = models.CharField(max_length=500)
    price = models.CharField(max_length=500)
    duration = models.TimeField()
    terminal = models.CharField(max_length=500)
    travel_class = models.CharField(max_length=500)
    airport = models.CharField(max_length=500)
    # deep_link = models.CharField()  # From here we purchase the flight
    #
    # def get_flight_details(self):
    #     pass
