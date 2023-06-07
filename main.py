import random
from typing import List

from dotenv import load_dotenv

import json
from src.path_finder import PathFinder
from src.dataclass.address import Address
from src.dataclass.booking import Booking
from src.google_maps_api import GoogleMapsApi
from src.helpers.time_converter import hours_to_seconds
from src.planner import Planner


def load_addresses() -> List[Address]:
    with open('json/addresses.json', 'r') as file:
        addresses = [Address(**data) for data in json.load(file)]
    return addresses


def load_praticien() -> Address:
    with open('json/praticien.json', 'r') as file:
        praticien = Address(**json.load(file))
    return praticien


def main():
    # load .env file
    load_dotenv()

    # load data
    google_api = GoogleMapsApi()
    praticien = load_praticien()
    addresses = load_addresses()
    #google_api.generate_all_distances(addresses)
    addresses_with_nb_visits = [(random.randint(2, 3), address) for address in addresses]
    first_booking = Booking.from_address(praticien, 1, 0, hours_to_seconds(8.0))
    last_booking = Booking.from_address(praticien, 2, 0, hours_to_seconds(18.0))
    fixed_bookings = [Booking.from_address(praticien, 3, hours_to_seconds(2.0), hours_to_seconds(13.0))]
    fixed_bookings = [first_booking] + fixed_bookings + [last_booking]
    planner = Planner(google_api, fixed_bookings,addresses_with_nb_visits)
    bookings = [Booking.from_address(address, idx + 4, hours_to_seconds(0.5), 0) for idx, address in
                enumerate(addresses)]

    path_finder = PathFinder(google_api, bookings, fixed_bookings)
    optimal_path = path_finder.calculate_path()
    print("Remaining bookings:")
    print("\n".join([str(booking) for booking in path_finder.bookings]))
    print("Optimal path:")
    print("\n".join([str(booking) for booking in optimal_path]))
    maps_itinerary = "/".join(["'{},{}'".format(booking.address.lat, booking.address.lng) for booking in optimal_path])
    print("https://www.google.com/maps/dir/{}?entry=ttu".format(maps_itinerary))

    print("Cached requests: {}".format(google_api.cached_requests))
    print("Api requests: {}".format(google_api.api_requests))


if __name__ == '__main__':
    main()
