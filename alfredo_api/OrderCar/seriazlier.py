from rest_framework import serializers

from alfredo_api.OrderCar.model import OrderCar


class OrderCarSerializer(serializers.ModelSerializer):
    # trip_id
    class Meta:
        model = OrderCar
        fields = ('address', 'long_position', 'lat_position',
                  'car_category', 'car_transmission', 'car_type',
                  'car_air_condition', 'car_fuel', 'company_code',
                  'is_on_airport', 'price')
