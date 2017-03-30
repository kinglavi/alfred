from django.db import models

class OrderHotel(models.Model):
  user_id = models.CharField()
  hotel_id = models.CharField()
  booking_code = models.CharField()
  room_type_code = models.CharField()
  rate_plan_code = models.CharField()
  descriptions = models.CharField()


  def get_hotel_details(self):
    # TODO: request get from the api.
    pass
