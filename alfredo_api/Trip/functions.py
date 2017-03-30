from alfredo_api.OrderCar.model import OrderCar
from alfredo_api.OrderCar.seriazlier import OrderCarSerializer
from alfredo_api.OrderFlight.model import OrderFlight
from alfredo_api.OrderFlight.seriazlier import OrderFlightSerializer
from alfredo_api.OrderHotel.model import OrderHotel
from alfredo_api.OrderHotel.seriazlier import OrderHotelSerializer
from alfredo_api.Trip.model import Trip
from alfredo_api.Trip.seriazlier import TripSerializer


def get_all_trips_by_user(user):
    t = TripSerializer(Trip.objects.filter(user=user)).data
    hotels = OrderHotel.objects.filter(trip=t)
    if len(hotels) == 1:
        hotel_json = OrderHotelSerializer(hotels).data
    elif len(hotels) > 1:
        hotel_json = OrderHotelSerializer(hotels, many=True).data
    else:
        hotel_json = []

    flights = OrderFlight.objects.filter(trip=t)
    if len(flights) == 1:
        flight_json = OrderFlightSerializer(flights).data
    elif len(flights) > 1:
        flight_json = OrderFlightSerializer(flights, many=True).data
    else:
        flight_json = []

    cars = OrderCar.objects.filter(trip=t)
    if len(cars) == 1:
        car_json = OrderCarSerializer(cars).data
    elif len(cars) > 1:
        car_json = OrderCarSerializer(cars, many=True).data
    else:
        car_json = []

    t['hotel'] = hotel_json
    t['flight'] = flight_json
    t['car'] = car_json
    return t
