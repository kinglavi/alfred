from rest_framework import serializers

from alfredo_api.OrderFlight.model import OrderFlight


class OrderFlightSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderFlight
        fields = ('origin', 'destination', 'departure_date',
                  'departure_time', 'arrival_date', 'arrival_time',
                  'air_line_name', 'flight_number', 'price',
                  'duration', 'terminal', 'travel_class')
