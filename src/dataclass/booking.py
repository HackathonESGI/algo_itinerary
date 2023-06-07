from dataclasses import dataclass
from typing import Optional

from src.dataclass.address import Address
from src.helpers.time_converter import seconds_to_hours_minutes


@dataclass
class Booking:
    address: Address
    stay_seconds: int
    date: str
    booking_time_seconds: Optional[int] = None
    to_reach_kms: Optional[float] = None
    to_reach_seconds: Optional[int] = None
    arrival_time_seconds: Optional[int] = None

    def update(self, to_reach_kms: float, to_reach_seconds: int, arrival_time_seconds: int):
        self.to_reach_kms = to_reach_kms
        self.to_reach_seconds = to_reach_seconds
        self.arrival_time_seconds = arrival_time_seconds
        if self.booking_time_seconds is None:
            self.booking_time_seconds = arrival_time_seconds

    @property
    def departure_time(self):
        return self.booking_time_seconds + self.stay_seconds\
            if self.stay_seconds is not None and self.booking_time_seconds is not None\
            else 0

    @property
    def free_time_seconds(self):
        return self.booking_time_seconds - self.arrival_time_seconds\
            if self.arrival_time_seconds is not None and self.booking_time_seconds is not None\
            else 0

    @classmethod
    def from_address(cls,
                     address: Address,
                     date: str,
                     stay_seconds: int,
                     booking_time_seconds: Optional[int] = None,
                     to_reach_kms: Optional[float] = None,
                     to_reach_seconds: Optional[int] = None
                     ):
        return cls(
            address,
            stay_seconds,
            date,
            booking_time_seconds,
            to_reach_kms,
            to_reach_seconds
        )

    def __str__(self):
        base = "{}".format(self.address)
        if self.arrival_time_seconds:
            base += " at {:02d}:{:02d} until {:02d}:{:02d}".format(*seconds_to_hours_minutes(self.arrival_time_seconds),
                                                                   *seconds_to_hours_minutes(self.departure_time))
        if self.to_reach_kms and self.to_reach_seconds:
            base += " after {}km and {:02d}:{:02d}".format(self.to_reach_kms,
                                                           *seconds_to_hours_minutes(self.to_reach_seconds))
        return base
