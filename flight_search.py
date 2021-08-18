from data_manager import DataManager
from flight_data import FlightData


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    # once the data has been found it should update the flight data in google sheets
    def get_iata_code(flight_data: FlightData):
        flight_data.city_iata_code = "Testing"
        DataManager.update_iata_code(flight_data=flight_data)
