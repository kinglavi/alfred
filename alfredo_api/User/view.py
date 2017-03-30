from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from alfredo_api.Trip.model import Trip
from alfredo_api.Trip.seriazlier import TripSerializer
from alfredo_api.User.functions import do_magic, do_magic_for_ui
from alfredo_api.User.seriazlier import UserSerializer
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST


class CampaignView(viewsets.ModelViewSet):
    """
        This is Campaign view set.
    """
    serializer_class = TripSerializer
    queryset = Trip.objects.all()


@api_view(['POST'])
def create_trip_option_view(request):
    date = request.data['date'] if 'date' in request.data else None
    star_count = request.data['starCount'] if 'starCount' in request.data else None
    flights_check = request.data['flightsCheck'] if 'flightsCheck' in request.data else None
    hotel_check = request.data['hotelCheck'] if 'hotelCheck' in request.data else None
    transportation_check = request.data['transportationCheck'] if 'transportationCheck' in request.data else None
    destination_address = request.data['destinationAddress'] if 'destinationAddress' in request.data else None
    origin_address = request.data['originAddress'] if 'originAddress' in request.data else None
    description = request.data['description'] if 'description' in request.data else None

    return Response(do_magic_for_ui(date, star_count, flights_check, hotel_check,
                                    transportation_check, destination_address,
                                    origin_address))


# def do_magic (req_type, origin, dest, arrive_by, rating):



@api_view(['POST'])
def create_auth(request):
    serialized = UserSerializer(data=request.DATA)
    if serialized.is_valid():
        User.objects.create_user(
            serialized.init_data['email'],
            serialized.init_data['username'],
            serialized.init_data['password']
        )
        return Response(serialized.data, status=HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=HTTP_400_BAD_REQUEST)
