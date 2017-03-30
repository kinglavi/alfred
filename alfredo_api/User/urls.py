from django.conf.urls import url

from alfredo_api.User.view import create_trip_option_view, create_auth

urlpatterns = [
    url(r'^users/register', create_auth),
    url(r'^getTrips', create_trip_option_view),
    ]
