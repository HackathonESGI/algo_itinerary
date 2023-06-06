from dataclasses import dataclass


@dataclass
class Address:
    id: int
    name: str
    lat: float
    lng: float

    def __str__(self):
        return f'{self.id}'

    @classmethod
    def from_booking(cls, booking: "Booking"):
        return cls(
            booking.id,
            booking.name,
            booking.lat,
            booking.lng
        )
