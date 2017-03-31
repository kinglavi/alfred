from rest_framework import viewsets
from rest_framework.decorators import api_view

from rest_framework.response import Response

from alfredo_api.OrderHotel.model import OrderHotel
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
    # if request.user is not None:
    username = request.query_params.get('username')
    return Response(get_all_trips_by_user(username))
    # else:
    #     return Response("User must be logged in.", 403)


# user = models.ForeignKey(User)
#     arrival_time = models.DateTimeField()
#     return_time = models.DateTimeField()
#     # Destination
#     address = models.CharField(max_length=500)
#     price = models.IntegerField()
#     current_address = models.CharField(max_length=500
# @api_view(['POST'])
# def save_trip(request):
#     t = Trip(user=request.user,
#              arrival_time=request.data['arrival_time'],
#              address=request.data['address'],
#              price=request.data['price'],
#              current_address=request.data['current_address'])
#
#     hotels = request.data['hotels']
#     [OrderHotel(h) for h in hotels]
