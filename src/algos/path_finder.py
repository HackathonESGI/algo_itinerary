from typing import List

from src.dataclass.booking import Booking
from src.google_maps_api import GoogleMapsApi
from src.helpers.time_converter import hours_to_seconds


class PathFinder:
    def __init__(self, google_api: GoogleMapsApi, bookings: List[Booking], fixed_bookings: List[Booking]):
        self.google_api = google_api
        self.bookings = bookings
        self.fixed_bookings = sorted(fixed_bookings, key=lambda x: x.arrival_time_seconds)
        self.path = []

    def calculate_path(self):
        if not self.fixed_bookings:
            return self.bookings
        for i in range(len(self.fixed_bookings) - 1):
            start = self.fixed_bookings[i]
            end = self.fixed_bookings[i + 1]
            path_segment = self._calculate_path_segment(start, end)
            self.path += path_segment

        return self.path + [self.fixed_bookings[-1]]

    def _calculate_path_segment(self, start: Booking, end: Booking) -> List[Booking]:
        last_booking = start
        last_booking_departure = last_booking.departure_time
        segment = [start]
        remaining_time = end.arrival_time_seconds - last_booking_departure
        while  self.bookings:
            best_booking = None
            best_duration = float('inf')
            best_distance = float('inf')
            for booking in self.bookings:
                distance, duration = self.google_api.get_distance_and_duration(last_booking.address, booking.address)
                if duration < best_duration and duration + booking.stay_seconds <= remaining_time:
                    best_booking = booking
                    best_duration = duration
                    best_distance = distance
            if best_booking:
                arrival_time = last_booking_departure + best_duration
                best_booking.update(
                    best_distance,
                    best_duration,
                    arrival_time
                )
                segment.append(best_booking)
                last_booking = best_booking
                last_booking_departure = last_booking.departure_time
                self.bookings.remove(best_booking)
                remaining_time = end.arrival_time_seconds - last_booking_departure
            else:
                break
            if remaining_time <= hours_to_seconds(0.1):
                break

        return segment
