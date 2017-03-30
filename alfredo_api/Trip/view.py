from rest_framework import viewsets
from rest_framework.decorators import api_view

from alfredo_api.Trip.model import Trip
from alfredo_api.Trip.seriazlier import TripSerializer


class TripView(viewsets.ModelViewSet):
    """
        This is Campaign view set.
    """
    serializer_class = TripSerializer
    queryset = Trip.objects.all()


@api_view(['GET'])
def get_trip_by_user(request, user_id):
    # if is_authenticated(user_id):
    # Trip.objects.filter(user=)
    pass