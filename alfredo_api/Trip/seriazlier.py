from rest_framework import serializers

from alfredo_api.Trip.model import Trip
from alfredo_api.User.seriazlier import UserSerializer


class TripSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Trip
        fields = ('id', 'added_time', 'arrival_time',
                  'return_time', 'address',
                   'record_locator','user')
