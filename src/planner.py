from typing import List, Tuple

from src.dataclass.address import Address
from src.dataclass.booking import Booking
from src.google_maps_api import GoogleMapsApi

def day_for_3(day: int):
    return day == 0 or day == 2 or day == 4

class Planner:
    def __init__(self, google_api:GoogleMapsApi, daily_fixed_bookings: List[Booking], fixed_booking:List[Booking], addresses:List[Tuple[int, Address]]):
        self.daily_fixed_bookings = daily_fixed_bookings
        self.fixed_bookings = fixed_booking
        self.google_api = google_api
        self.addresses = addresses
        self.paths = [[] for i in range(5)]
        self.missed_booking_addresses = []


    def plan(self):
        for day in range(5):
            self._plan_day(day)
        return self.paths

    def get_addresses_by_day(self, day: int):
        number_of_visit_by_week = 3 if day_for_3(day) else 2
        return self.missed_booking_addresses +  [address for nb_days, address in self.addresses if nb_days == number_of_visit_by_week]

    def get_fixed_bookings_by_day(self, day: int):
        pass

    def _plan_day(self, day):
        addresses = self.get_addresses_by_day(day)
        if not addresses:
            return
        fixed_bookings = self.daily_fixed_bookings


