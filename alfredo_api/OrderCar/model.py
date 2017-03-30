from django.db import models

from alfredo_api.Trip.model import Trip


class OrderCar(models.Model):
    trip = models.ForeignKey(Trip)
    address = models.CharField(max_length=500)
    long_position = models.DecimalField(max_digits=8, decimal_places=3)
    lat_position = models.DecimalField(max_digits=8, decimal_places=3)
    car_category = models.CharField(max_length=500)
    car_transmission = models.CharField(max_length=500)
    car_type = models.CharField(max_length=500)
    car_air_conditioning = models.CharField(max_length=500)
    car_fuel = models.CharField(max_length=500)
    company_code = models.CharField(max_length=500)
    is_on_airport = models.BooleanField()
    price = models.IntegerField()

    # def get_agency_details(self):
    #     pass
