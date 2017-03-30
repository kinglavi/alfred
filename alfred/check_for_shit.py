import requests

req_url = 'http://'

def will_shit_happen_to_me():

  # amadeus response for the request
  user_orders = requests.get(req_url)

  if user_orders.status_code != 200:
    return 'ERROR - no orders'
  else:
    response_json = user_orders.json()

  for flight in user_orders['flights']:
    pass
