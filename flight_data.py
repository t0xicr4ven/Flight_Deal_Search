class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, city_name, city_iata_code, lowest_price, city_sheety_id):
        self.city_name = city_name
        self.city_iata_code = city_iata_code
        self.lowest_price = lowest_price
        self.city_sheety_id = city_sheety_id
