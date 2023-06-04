import uuid
from datetime import datetime
from geopy.geocoders import Nominatim


class Report:

    def __init__(self, rep_type, latitude, longitude):
        self.id = str(uuid.uuid4())
        self.date = datetime.now()
        self.crime_type = None
        self.intensity = 0
        self.verified = False
        self.address = None
        self.crime_type = " "

        self.type = rep_type
        self.latitude = latitude
        self.longitude = longitude

    def display(self):
        print(f"Type: {self.type}")
        print(f"Location: {self.address}")

    def is_verified(self):
        return self.verified

    def set_verified(self):
        self.verified = True

        return self.verified

    def calculate_report_intensity(self):

        if self.crime_type == "robbery":
            self.intensity = 0.1
        elif self.crime_type == "vandalism":
            self.intensity = 0.07
        elif self.crime_type == "mugging":
            self.intensity = 0.05
        else:
            self.intensity = 1

        return self.intensity

    def coordinates_to_address(self):
        # Create a geolocator object
        geolocator = Nominatim(user_agent="my_app")

        # Reverse geocode the coordinates
        location = geolocator.reverse(f"{self.latitude}, {self.longitude}")

        # Extract the address from the location object
        self.address = location.address

        return self.address

"""
        robbery 0.1
        shoplifting 0.1
        murder 0.2
        vandalism 0.05

        arson(fire)
        mugging
"""