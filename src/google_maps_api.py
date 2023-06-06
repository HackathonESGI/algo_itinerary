import json
import os
from typing import Optional, Dict, Tuple, List

import requests as requests

from src.dataclass.address import Address
from src.dataclass.booking import Booking


class GoogleMapsApi:
    """
        The GoogleMapsApi class provides functionality to interact with the Google Maps Directions API.
        It contains methods for getting the distance and duration between two addresses,
        and for caching the results of these API requests.
    """
    cache: Dict[str, tuple[Optional[float], Optional[int]]]

    def __init__(self):
        self.api_key = os.getenv('GOOGLE_MAPS_API_KEY')
        self._load_cache()

    def generate_all_distances(self, addresses:List[Address]):
        for address in addresses:
            for address2 in addresses:
                if address.id != address2.id:
                    self.get_distance_and_duration(address, address2)


    def get_distance_and_duration(self, origin: Address , destination: Address ,
                                  departure_timestamp: Optional[int]= None) -> \
    tuple[Optional[float], Optional[int]]:
        """
        Get the distance and duration between two addresses.
        :param origin: obj lat and lng
        :param destination: obj lat and lng
        :return: distance in km, duration in seconds
        """

        cache_slug = self._get_direction_slug(origin, destination)
        if self._has_cache(cache_slug):
            return self._get_cache(cache_slug)

        end_point = 'https://maps.googleapis.com/maps/api/directions/json'
        params = {
            'origin': "{}, {}".format(origin.lat, origin.lng),
            'destination': "{}, {}".format(destination.lat, destination.lng),
            "mode": "driving",
            'key': self.api_key
        }
        if departure_timestamp:
            params['departure_time'] = departure_timestamp
        response = requests.get(end_point, params=params)
        if response.status_code == 200:
            response = response.json()
            distance = response['routes'][0]['legs'][0]['distance']['value'] / 1000
            duration = response['routes'][0]['legs'][0]['duration']['value']
            self._set_cache(cache_slug, distance, duration)
            return distance, duration
        else:
            raise Exception("Google Maps API returned status code {}".format(response.status_code))

    def _has_cache(self, cache_slug: str) -> bool:
        return cache_slug in self.cache

    def _get_cache(self, cache_slug: str) -> Tuple[Optional[float], Optional[int]]:
        return self.cache[cache_slug]

    def _set_cache(self, cache_slug: str, distance: float, duration: int):
        self.cache[cache_slug] = (distance, duration)
        self._save_cache()

    @staticmethod
    def _get_direction_slug(origin: Address , destination: Address ) -> str:
        return "{}_{}".format(origin.id, destination.id)

    def _load_cache(self):
        with open('json/g_api_cache.json', 'r') as file:
            self.cache = json.load(file)

    def _save_cache(self):
        with open('json/g_api_cache.json', 'w') as file:
            # ordered_cache = {key: self.cache[key] for key in sorted(self.cache.keys(), key=lambda x: (int(x.split('_')[0]), int(x.split('_')[1])))}
            # self.cache = ordered_cache
            json.dump(self.cache, file)
