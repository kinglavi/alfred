from django.db import models

class OrderHotel(models.Model):
  user_id = models.CharField()
  hotel_id = models.CharField()
  booking_code = models.CharField()
  room_type_code = models.CharField()
  transmision = models.CharField()
  car_Type = models.CharField()
  air_conditioning = models.CharField()


  def get_hotel_details(self):
    # TODO: request get from the api.
    pass
