import datetime
import random
from typing import List, Tuple

from dotenv import load_dotenv
from tabulate import tabulate

import json
from src.dataclass.address import Address
from src.dataclass.booking import Booking
from src.dataclass.fixed_recurrent_booking import FixedRecurrentBooking
from src.dataclass.variable_recurrent_booking import VariableRecurrentBooking
from src.google_maps_api import GoogleMapsApi
from src.helpers.time_converter import hours_to_seconds, seconds_to_time
from src.planner import Planner


BASE_START_DATE = '2021-01-01'
BASE_END_DATE = '2023-12-31'

def load_addresses() -> List[Address]:
    with open('json/addresses.json', 'r') as file:
        addresses = [Address(**data) for data in json.load(file)]
    return addresses


def load_praticien() -> Address:
    with open('json/praticien.json', 'r') as file:
        praticien = Address(**json.load(file))
    return praticien


def generate_fake_bookings(praticien: Address, addresses: List[Address]) -> Tuple[
    List[FixedRecurrentBooking], List[VariableRecurrentBooking], List[Booking]]:
    start_of_day = FixedRecurrentBooking(praticien, 0, BASE_START_DATE, BASE_END_DATE, hours_to_seconds(8.0),
                                         [0, 1, 2, 3, 4])
    end_of_day = FixedRecurrentBooking(praticien, 0, BASE_START_DATE, BASE_END_DATE, hours_to_seconds(18.0),
                                       [0, 1, 2, 3, 4])
    fixed_recurrent_bookings = [start_of_day, end_of_day]
    # set fixed bookings for each day of the next current week at 12:00 to 14:00
    today = datetime.datetime.now().date()
    start_of_next_week = today + datetime.timedelta(days=(7 - today.weekday() + 1) % 7)  # Get the date of the next week
    fixed_bookings = []
    for day in range(5):
        booking_date = start_of_next_week + datetime.timedelta(days=day)
        fixed_bookings.append(Booking.from_address(praticien, booking_date.strftime('%Y-%m-%d'), hours_to_seconds(2.0), hours_to_seconds(12.0)))

    variable_recurrent_bookings = []
    for address in addresses:
        # random between 2 and 3 visits per week
        per_week = random.randint(2, 3)
        variable_recurrent_bookings.append(
            VariableRecurrentBooking(address, hours_to_seconds(0.5), BASE_START_DATE, BASE_END_DATE, per_week)
        )
    return fixed_recurrent_bookings, variable_recurrent_bookings, fixed_bookings

def main():
    # load .env file
    load_dotenv()

    # load data
    google_api = GoogleMapsApi()
    praticien = load_praticien()
    addresses = load_addresses()
    fixed_recurrent_bookings, variable_recurrent_bookings, fixed_bookings = generate_fake_bookings(praticien, addresses)
    planner = Planner(google_api, fixed_recurrent_bookings, variable_recurrent_bookings, fixed_bookings)
    paths = planner.plan("2023-06-12")

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    for i, path in enumerate(paths):
        print(f"\n\n{days[i]}")
        table = []
        for booking in path:
            table.append([booking.address.name, seconds_to_time(booking.arrival_time_seconds),
                          seconds_to_time(booking.departure_time), booking.to_reach_kms, seconds_to_time(booking.to_reach_seconds) if booking.to_reach_seconds else None])
        print(tabulate(table, headers=['Address', 'Arrival Time', 'Departure Time', 'Kms to reach', 'Time to reach' ]))
        maps_itinerary = "/".join(
            ["{},{}".format(booking.address.lat, booking.address.lng) for booking in path])
        print("\nUrl: https://www.google.com/maps/dir/{}?entry=ttu".format(maps_itinerary))

    print("\n")
    print("Missed bookings:")
    if planner.missed_booking_addresses:
        missed_table = []
        for booking in planner.missed_booking_addresses:
            missed_table.append([booking.address.name])
        print(tabulate(missed_table, headers=['Missed Address']))
    else:
        print("No missed bookings.")
    print()
    print("Cached requests: {}".format(google_api.cached_requests))
    print("Api requests: {}".format(google_api.api_requests))


if __name__ == '__main__':
    main()
