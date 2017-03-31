from django.conf.urls import url

from alfredo_api.Trip.view import get_trip_by_user

urlpatterns = [
    url(r'^api/getTripsByUser', get_trip_by_user),
    ]
