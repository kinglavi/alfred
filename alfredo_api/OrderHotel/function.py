import requests

from alfredo_api.conf import AMADEUS_URL, API_KEY


def get_hotel_details(property_code, check_in, check_out):
    url = "%s/hotels/%s?check_in=%s&check_out=%s&apikey=%s" % \
          (AMADEUS_URL, property_code, check_in, check_out, API_KEY)

    try:
        res = requests.get(url=url)
    except Exception as e:
        raise("Problem with amadeus api. reason: %s" % e.message)

    return res.json()
