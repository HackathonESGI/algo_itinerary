from abc import ABC, abstractmethod
from typing import List

from src.dataclass.booking import Booking
from src.google_maps_api import GoogleMapsApi


class BasePathFinder(ABC):
    def __init__(self, google_api: GoogleMapsApi, fixed_bookings: List[Booking], bookings: List[Booking]):
        self.google_api = google_api
        self.bookings = bookings
        self.fixed_bookings = sorted(fixed_bookings, key=lambda x: x.booking_time_seconds)
        self.path = []



    def calculate_path(self):
        if not self.fixed_bookings:
            return self.bookings
        for i in range(len(self.fixed_bookings) - 1):
            start = self.fixed_bookings[i]
            end = self.fixed_bookings[i + 1]
            path_segment = self._calculate_path_segment(start, end)
            self.path += path_segment[1:] if len(path_segment) > 1 else path_segment
            print()

        return [self.fixed_bookings[0]] + self.path

    @abstractmethod
    def _calculate_path_segment(self, start: Booking, end: Booking) -> List[Booking]:
        pass