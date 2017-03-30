from django.db import models

class Hotlel(models.Model):
  hotle_name = models.CharField()
  long_position = models.DecimalField(max_digits=8, decimal_places=3)
  lat_position = models.DecimalField(max_digits=8, decimal_places=3)
  address_city = models.CharField()
  address_country = models.CharField()
  addresss = models.CharField()
  phone =  models.CharField()
