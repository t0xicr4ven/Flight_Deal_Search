import os
import requests
from flight_search import FlightSearch
from flight_data import FlightData
from data_manager import DataManager
# from pprint import pprint


SHEETY_ENDPOINT = os.environ.get('flight_search_sheety_endpoint')


response = requests.get(url=SHEETY_ENDPOINT)
data = response.json()
sheet_data = data#['prices']
print(sheet_data)
# turn each entry into an object
for place in sheet_data:
    iataCode = place['iataCode']
    city = place['city']
    city_id = place['id']
    city_lowest_price = place['lowestPrice']
    if iataCode == "":
# if its a new entry by user, it might not have the iata code so we will have to go search for it and alter the sheet
        new_city = FlightData(city_name=city, city_iata_code=iataCode,
                          city_sheety_id=city_id, lowest_price=city_lowest_price)
        new_city.city_iata_code = FlightSearch.get_iata_code(new_city)
        DataManager.update_iata_code(new_city)
