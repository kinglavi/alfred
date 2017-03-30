from django.db import models

class OrderFilght(models.Model):
  user_id = models.CharField()
  origin = models.CharField()
  destination = models.CharField()
  departure_date = models.DateField()
  departure_time = models.DateTimeField()
  arrival_date = models.DateTimeField()
  arrival_time = models.DateTimeField()
  air_line = models.CharField()
  flight_number = models.CharField()
  deep_link = models.CharField() #  From here we purchase the flight


