import datetime
from dataclasses import dataclass
from typing import Optional

from src.dataclass.address import Address
from src.dataclass.base_recurrent_booking import BaseRecurrentBooking
from src.dataclass.booking import Booking


@dataclass
class FixedRecurrentBooking(BaseRecurrentBooking):
    arrival_time_seconds: int
    days_of_week: list[int]

    def can_book(self, date: datetime.datetime) -> bool:
        day_of_week = date.weekday()
        date_string = date.strftime("%Y-%m-%d")
        if self.start_date > date_string:
            return False
        if self.end_date < date_string:
            return False
        if day_of_week not in self.days_of_week:
            return False
        return True

    def get_booking(self, date: datetime.datetime) -> Optional[Booking]:
        if not self.can_book(date):
            return None
        return Booking.from_address(
            self.address,
            date.strftime("%Y-%m-%d"),
            self.stay_seconds,
            self.arrival_time_seconds
        )
