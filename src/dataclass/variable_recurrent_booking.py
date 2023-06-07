import datetime
from dataclasses import dataclass
from typing import Optional

from src.dataclass.base_recurrent_booking import BaseRecurrentBooking
from src.dataclass.booking import Booking


@dataclass
class VariableRecurrentBooking(BaseRecurrentBooking):
    days_per_week: int

    def get_days_of_week(self) -> list[int]:
        if self.days_per_week == 3:
            return [0, 2, 4]
        if self.days_per_week == 2:
            return [1, 3]

    def can_book(self, date: datetime.datetime) -> bool:
        date_str = date.strftime("%Y-%m-%d")
        day_of_week = date.weekday()
        if day_of_week not in self.get_days_of_week():
            return False
        if self.start_date > date_str:
            return False
        if self.end_date < date_str:
            return False
        return True

    def get_booking(self, date: datetime.datetime) -> Optional[Booking]:
        if not self.can_book(date):
            return None
        return Booking.from_address(
            self.address,
            date.strftime("%Y-%m-%d"),
            self.stay_seconds,
        )
