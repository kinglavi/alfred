import requests
from django.db import models

from alfredo_api.Trip.model import Trip
# from alfredo_api.conf import AMADEUS_URL, API_KEY


class OrderHotel(models.Model):
    trip = models.ForeignKey(Trip)
    check_in = models.DateField()
    check_out = models.DateField()
    booking_code = models.CharField(max_length=500)
    room_type_code = models.CharField(max_length=500)
    rate_plan_code = models.CharField(max_length=500)
    room_descriptions = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    room_type = models.CharField(max_length=500)
    price = models.IntegerField()

    # def get_hotel_details(self):
    #     # TODO: request get hotel details from hotel_id
    #     url = "%s/hotels/%s?check_in=%s&check_out=%s&apikey=%s" % \
    #           (AMADEUS_URL, self.property_code, self.check_in, self.check_out, API_KEY)
    #     requests.get(url=url)
