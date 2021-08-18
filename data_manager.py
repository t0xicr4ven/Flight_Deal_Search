from flight_data import FlightData
import requests
import os

SHEETY_BASE_ENDPOINT = os.environ.get('flight_search_sheety_endpoint')


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def update_iata_code(flight_data: FlightData):
        body = {
            'price': {
                'iataCode': flight_data.city_iata_code,
            }
        }
        put_response = requests.put(
            url=f"{SHEETY_BASE_ENDPOINT}/{flight_data.city_sheety_id}", json=body)
        print(put_response.text)
