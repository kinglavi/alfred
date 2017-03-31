import requests

req_url = 'http://'
CHECK_FOR_PROBABILITY_API = 'http://localhost:8080/api/predict/'

def will_shit_happen_to_me():

  # amadeus response for the request
  user_orders = requests.get(req_url)

  if user_orders.status_code != 200:
    return 'ERROR - no orders'
  else:
    response_json = user_orders.json()

  for flight in user_orders['flights']:

    flight_date_formated = flight['departure_date'] + flight['departure_time']
    probobility = requests.get(CHECK_FOR_PROBABILITY_API + flight['airport'] + '/' + flight_date_formated + '/')

    if probobility == 'RED':
      # call the push notification for flight
      pass
    elif probobility == 'YELLOW':
      # call the push notification
      pass

