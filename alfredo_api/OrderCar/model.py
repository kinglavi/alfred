from django.db import models

class OrderCar(models.Model):
  user_id = models.CharField()
  long_position = models.DecimalField(max_digits=8, decimal_places=3)
  lat_position = models.DecimalField(max_digits=8, decimal_places=3)
  category = models.CharField()
  transmision = models.CharField()
  car_Type = models.CharField()
  air_conditioning = models.CharField()


  def get_agency_details(self):
    # TODO: request get from the api.
    pass
