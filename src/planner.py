import datetime
from typing import List

from src.dataclass.booking import Booking
from src.dataclass.fixed_recurrent_booking import FixedRecurrentBooking
from src.dataclass.variable_recurrent_booking import VariableRecurrentBooking
from src.google_maps_api import GoogleMapsApi
from src.path_finders.bfs_path_finder import BfsPathFinder


class Planner:
    def __init__(self, google_api: GoogleMapsApi, fixed_recurrent_bookings: List[FixedRecurrentBooking],
                 variable_recurrent_booking: List[VariableRecurrentBooking], fixed_bookings: List[Booking]):
        self.google_api = google_api
        self.fixed_recurrent_bookings = fixed_recurrent_bookings
        self.variable_recurrent_booking = variable_recurrent_booking
        self.fixed_bookings = fixed_bookings
        self.paths = [[] for _ in range(5)]
        self.missed_booking_addresses = []

    def plan(self, start_date: str):
        date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        if date.weekday() != 0:
            raise Exception("Start date should be a monday")
        for day_of_week in range(5):
            date_of_day = date + datetime.timedelta(days=day_of_week)
            self._plan_day(date_of_day)
        return self.paths

    def _get_bookings_from_fixed_bookings(self, date: datetime.datetime) -> List[Booking]:
        return [booking for booking in self.fixed_bookings if booking.date == date.strftime("%Y-%m-%d")]

    def _get_bookings_from_fixed_recurrent_bookings(self, date: datetime.datetime) -> List[Booking]:
        return [
            fixed_recurrent_booking.get_booking(date)
            for fixed_recurrent_booking in self.fixed_recurrent_bookings
            if fixed_recurrent_booking.can_book(date)
        ]

    def _get_bookings_from_variable_recurrent_bookings(self, date: datetime.datetime) -> List[Booking]:
        return [
            variable_recurrent_booking.get_booking(date)
            for variable_recurrent_booking in self.variable_recurrent_booking
            if variable_recurrent_booking.can_book(date)
        ]

    def _plan_day(self, date: datetime.datetime):
        # find fixed bookings of the day
        # find fixed_recurrent_bookings of the day
        # find variable_recurrent_bookings of the day
        fixed_bookings = self._get_bookings_from_fixed_bookings(date) \
                         + self._get_bookings_from_fixed_recurrent_bookings(date)
        bookings = self.missed_booking_addresses + self._get_bookings_from_variable_recurrent_bookings(date)
        path_finder = BfsPathFinder(self.google_api, fixed_bookings, bookings)
        path = path_finder.calculate_path()
        self.missed_booking_addresses = path_finder.bookings
        self.paths[date.weekday()] = path
