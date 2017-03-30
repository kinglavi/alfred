from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from alfredo_api.Trip.functions import get_all_trips_by_user
from alfredo_api.Trip.model import Trip
from alfredo_api.Trip.seriazlier import TripSerializer


class TripView(viewsets.ModelViewSet):
    """
        This is Campaign view set.
    """
    serializer_class = TripSerializer
    queryset = Trip.objects.all()


@api_view(['GET'])
def get_trip_by_user(request):
    # if is_authenticated(user_id):
    # Trip.objects.filter(user=)
    if request.user is not None:
        return Response(get_all_trips_by_user(request.user))
    else:
        return Response("User must be logged in.", 403)
