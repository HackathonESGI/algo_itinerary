import datetime
from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.dataclass.address import Address
from src.dataclass.booking import Booking


@dataclass
class BaseRecurrentBooking(ABC):
    address: Address
    stay_seconds: int
    start_date: str
    end_date: str

    @abstractmethod
    def can_book(self, date: datetime.datetime) -> bool:
        pass

    @abstractmethod
    def get_booking(self, date: datetime.datetime) -> "Booking":
        pass