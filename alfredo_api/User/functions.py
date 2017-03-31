# imports
import requests
import re

from datetime import datetime, timedelta

# consts
from django.contrib.auth.models import User

from alfredo_api.OrderFlight.model import OrderFlight
from alfredo_api.OrderHotel.model import OrderHotel
from alfredo_api.Trip.model import Trip

AMADEUS_API_KEY = 'j8GYYZ3bPY1SDG6udDhsQ7ZVqz6hBsDD'
FLIGHT_SEARCH_API_URL = 'https://api.sandbox.amadeus.com/v1.2/flights/affiliate-search?'
HOTEL_SEARCH_API_URL = 'https://api.sandbox.amadeus.com/v1.2/hotels/search-circle?'
CAR_SEARCH_API_URL = 'https://api.sandbox.amadeus.com/v1.2/cars/search-circle?'
CITY_CONV_API_URL = 'https://api.sandbox.amadeus.com/v1.2/airports/autocomplete'
CITY_IATA_CONV_API = 'https://api.sandbox.amadeus.com/v1.2/points-of-interest/yapq-search-text?'
DATE_TIME_FORMAT = '%Y-%m-%dT%H:%M:%S'
DATE_FORMAT = '%Y-%m-%d'


# help functions
def build_flight_req(destination, origin, departure_date_time):
    # build the flight params
    flight_details = ''
    flight_details += 'origin=' + origin + '&'
    flight_details += 'destination=' + destination + '&'
    flight_details += 'departure_date=' + departure_date_time.strftime(DATE_FORMAT)

    # return flight params
    return flight_details


def build_hotel_req(dest_x, dest_y, radius, checkin_date, checkout_date, number_of_results):
    result = ''
    result += 'latitude=' + repr(dest_x) + '&longitude=' + repr(
        dest_y) + '&radius=' + radius + '&check_in=' + checkin_date.strftime(
        DATE_FORMAT) + '&check_out=' + checkout_date.strftime(DATE_FORMAT) + '&number_of_results=' + number_of_results
    return result


def build_car_req(destination, origin, departue_date_time):
    car_details = ''


def get_amadeus_flight_data(req_url):
    # send the request
    req_url += '&apikey=' + AMADEUS_API_KEY

    # amadeus response for the request
    amadeus_response = requests.get(req_url)

    if amadeus_response.status_code != 200:
        return 'ERROR'
    else:
        response_json = amadeus_response.json()

    return response_json


def get_3_flights_from(data, start_index, end_index):
    result = []
    run = 0

    while run != -1:
        result.append(data[start_index])

        start_index += 1

        if start_index > end_index:
            run = -1
        else:
            run += 1

    return result


def get_top_routs(amadeus_fligth_data, rating):
    i = 1
    count = 0
    count_options = 0
    result = []

    # check if the route is a good one, and if so put it in the results array
    for route in amadeus_fligth_data:
        if route['will_make_it_on_time'] == "1" and route['is_premium'] == "1":
            # move the needed route to the result mto be returned
            result.append(route)

            # count the amound of results for rating
            count_options += 1

        count += 1

    # some really stupid logic, don't try to understand this shit
    if count_options >= 3:
        if rating >= 4:
            return get_3_flights_from(result, 0, 2)

        elif rating >= 2:
            if count >= 4:
                return get_3_flights_from(result, 1, 3)
            else:
                return get_3_flights_from(result, 0, 2)

        else:

            if count >= 5:
                return get_3_flights_from(result, 2, 4)

            else:
                return get_3_flights_from(result, 0, 2)

    else:
        if count_options == 0:
            if count > 0:
                return get_3_flights_from(amadeus_fligth_data, 0, 2)
            else:
                return 'ERROR'

        elif count_options == 1:
            return result

        else:
            return get_3_flights_from(result, 0, 1)


def rate_results(amadeus_fligth_data, arravial_date_time, rating):
    # for each flight route check the time of arrival
    for route_option in amadeus_fligth_data:
        # find the last flight in the route and check the arrival time, if it is good than add a rating to it
        for flight in route_option['outbound']['flights']:
            last_flight = flight

        # if the user will make it on time we will mark so
        if last_flight['arrives_at'] < arravial_date_time:
            route_option['will_make_it_on_time'] = "1"
        else:
            route_option['will_make_it_on_time'] = "0"

        # if the class of the flight is BUSINESS or FIRST we mark it
        if last_flight['booking_info']['travel_class'] == 'FIRST' or last_flight['booking_info'][
            'travel_class'] == 'BUSINESS' or last_flight['booking_info']['travel_class'] == 'PREMIUM_ECONOMY':
            route_option['is_premium'] = "1"
        else:
            route_option['is_premium'] = "0"

    return get_top_routs(amadeus_fligth_data, rating)


def get_amadeus_airport_data(url):
    # amadeus response for the request
    amadeus_response = requests.get(url)

    if amadeus_response.status_code != 200:
        return 'ERROR'
    else:
        response_json = amadeus_response.json()

    return response_json


# -----------------------------------------------------------------------
# more fun
def get_trip(req_type, rating, destination, origin, arravial_date_time, dest_x, dest_y):
    # req_type =====> 1 - flight  2 - car  3 - hotel

    # request url to send
    final_request_url = ''

    # calc a departue time
    departue_date_full = datetime.strptime(arravial_date_time, DATE_TIME_FORMAT)

    # build the request url by the params
    if req_type == 1:  # flight

        # do stuff for flight

        departue_date = departue_date_full
        # departue_date = departue_date_full - datetime.timedelta(days=1) this should substreact a day from the arrival date
        flight_params = build_flight_req(destination, origin, departue_date)
        final_request_url += FLIGHT_SEARCH_API_URL + flight_params

        # here we have the json of the result from amadeus
        amadeus_fligth_data = get_amadeus_flight_data(final_request_url)

        if amadeus_fligth_data == 'ERROR':
            return 'ERROR'
        else:
            return rate_results(amadeus_fligth_data['results'], arravial_date_time, rating)


    elif req_type == 2:  # car

        # do stuf for car
        car_params = build_car_req(destination, origin, departue_date_full)
        final_request_url += CAR_SEARCH_API_URL

    elif req_type == 3:  # hotel

        # do stuf for hotel
        hotel_params = build_hotel_req(dest_x, dest_y, '7', departue_date_full, departue_date_full + timedelta(days=2),
                                       '3')
        hotels = get_amadeus_flight_data(HOTEL_SEARCH_API_URL + hotel_params)

        return hotels

    else:
        return "Not a valid request type"


def do_magic(req_type, origin, dest, arrive_by, rating):
    if req_type == 1:

        origin_url = CITY_CONV_API_URL + '?apikey=' + AMADEUS_API_KEY + '&term=' + origin
        dest_url = CITY_CONV_API_URL + '?apikey=' + AMADEUS_API_KEY + '&term=' + dest

        origin_airports = get_amadeus_airport_data(origin_url)
        dest_airports = get_amadeus_airport_data(dest_url)

        # if there are air ports to select from, go over all airports and try to do magic
        if origin_airports != 'ERROR' and dest_airports != 'ERROR':
            for origin_airport in origin_airports:
                for dest_airport in dest_airports:
                    result = get_trip(req_type, rating, dest_airport['value'], origin_airport['value'], arrive_by, 0, 0)

                    if result != 'ERROR':
                        return result

        return 'ERROR - no flights'
    elif req_type == 3:

        # get city x and y for hotel search
        city_data_url = CITY_IATA_CONV_API + 'city_name=' + dest

        # here we have the city data
        city = get_amadeus_flight_data(city_data_url)

        print(rating)
        print(dest)
        print(origin)
        print(arrive_by)
        print(city['current_city']['location']['latitude'])
        print(city['current_city']['location']['longitude'])

        result = get_trip(3, rating, dest, origin, arrive_by, city['current_city']['location']['latitude'],
                          city['current_city']['location']['longitude'])

        if result != 'ERROR':
            return result
        else:
            return 'ERROR - no hotels'

    elif req_type == 2:
        pass
    else:
        return 'ERROR - NO REQ TYPE'


def do_magic_for_ui(date, star_count, flights_check, hotel_check,
                    transportation_check, destination_address,
                    origin_address):
    result = {}

    dest_city = destination_address.split(',')
    origin_city = origin_address.split(',')

    if flights_check:
        result['flights'] = do_magic(1, origin_city[0], dest_city[0], date, star_count)

    if hotel_check:
        result['hotels'] = do_magic(3, origin_city[0], dest_city[0], date, star_count)
    try:
        u=User(username="lssddsa",password="fgfsdgf")
        u.save()
        t = Trip(user=u, arrival_time=datetime.strptime(date, DATE_TIME_FORMAT) - timedelta(days=1),
                 return_time=datetime.strptime(date, DATE_TIME_FORMAT), address=destination_address)
        t.save()
        hotel_details = create_order_hotel_from_api_hotel(result['hotels']['results'][0])
        print hotel_details
        hotel = OrderHotel(trip=t, **hotel_details)
        hotel.save()
        flight_details = create_flight_order_from_api(result['flights'][0],
                                                      origin_city[0], dest_city[0],
                                                      datetime.strptime(date, DATE_TIME_FORMAT))
        flight = OrderFlight(trip=t, **flight_details)
        flight.save()
    except Exception as e:
        pass
    return result


# added_time = models.DateTimeField(auto_now=True)
# user = models.ForeignKey(User)
# arrival_time = models.DateTimeField()
# return_time = models.DateTimeField()
# # Destination
# address = models.CharField(max_length=500)
# price = models.IntegerField()
# current_address = models.CharField(max_length=500)
# # details for the flight
# record_locator = models.CharField(max_length=500, blank=True)


def create_flight_order_from_api(flight, origin_city, dest_city, date):
    return {
        "origin": origin_city,
        "destination": dest_city,
        "departure_datetime": flight['outbound']['flights'][0]['departs_at'],
        "arrival_date": date,
        "arrival_time": flight['outbound']['flights'][0]['arrives_at'],
        "air_line_name": flight['outbound']['flights'][0]['operating_airline'],
        "flight_number": flight['outbound']['flights'][0]['flight_number'],
        "price": flight['fare']['total_price'] + " " + flight['fare']['currency'],
        "duration": flight['outbound']['duration'],
        "terminal": flight['outbound']['flights'][0]['destination']['terminal'],
        "travel_class": flight['outbound']['flights'][0]['booking_info']['travel_class'],
        "airport": flight['outbound']['flights'][0]['origin']['airport']
    }


def create_order_hotel_from_api_hotel(api_hotel):
    return {
        "check_in": api_hotel['rooms'][0]['rates'][0]['start_date'],
        "check_out": api_hotel['rooms'][0]['rates'][0]['end_date'],
        "booking_code": api_hotel['rooms'][0]['booking_code'],
        "room_type_code": api_hotel['rooms'][0]['room_type_code'],
        "rate_plan_code": api_hotel['rooms'][0]['rate_plan_code'],
        "room_descriptions": api_hotel['rooms'][0]['descriptions'],
        "address": create_address_from_api_address(api_hotel['address']),
        "phone": [c['detail'] for c in api_hotel['contacts'] if c['type'] == 'PHONE'][0],
        "room_type": api_hotel['rooms'][0]['room_type_code'],
        "price": api_hotel['rooms'][0]['total_amount']['amount'] + " " + api_hotel['rooms'][0]['total_amount'][
            'currency'],
    }


def create_address_from_api_address(api_address):
    return api_address['country'] + " " + api_address['city'] + " " + \
           api_address['line1'] + " " + api_address['postal_code']
