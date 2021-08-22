import os
import requests
from data_manager import DataManager
from flight_data import FlightData

TEQUILA_ENDPOINT = os.environ.get('tequila_location_endpoint')
TEQUILA_API_KEY = os.environ.get('tequila_api_key')


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    # once the data has been found it should update the flight data in google sheets

    def get_iata_code(flight_data: FlightData):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        print(location_endpoint)
        teq_header = {
            "apikey": TEQUILA_API_KEY
            }
    
        body = {
            "location_types": "city",
            "term": flight_data.city_name,
            }
        response = requests.get(url=location_endpoint, params=body, headers=teq_header)
        result = response.json()['locations']
        return result[0]['code']
