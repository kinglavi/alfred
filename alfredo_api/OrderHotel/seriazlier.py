from rest_framework import serializers

from alfredo_api.OrderHotel.model import OrderHotel


class OrderHotelSerializer(serializers.ModelSerializer):
    # trip_id
    class Meta:
        model = OrderHotel
        fields = ('check_in', 'check_out', 'booking_code',
                  'room_type_code', 'rate_plan_code', 'room_descriptions'
                  'address', 'phone', 'room_type', 'price')
