from rest_framework import viewsets

from alfredo_api.Trip.model import Trip
from alfredo_api.Trip.seriazlier import TripSerializer


class CampaignView(viewsets.ModelViewSet):
    """
        This is Campaign view set.
    """
    serializer_class = TripSerializer
    queryset = Trip.objects.all()
