# Optimal Itinerary Planner

The Optimal Itinerary Planner is a Python application that leverages the Google Maps Directions API to plan optimal travel itineraries. It takes into account various addresses and bookings, sorting them optimally to minimize travel duration. It's especially useful for professionals who need to make multiple visits in a day, such as healthcare practitioners, salespeople, or delivery drivers.


## Features
- Load addresses from a JSON file. 
- Compute optimal itinerary using Google Maps Directions API. 
- Manage bookings, including fixed bookings with defined arrival times.
- Cache Google Maps API results for reuse to optimize API usage.
- Environment variable management for API keys.


## Setup
Prerequisites:
- Python 3.7+
- Google Maps Directions API key

## Installation
1. Clone the repository.
2. Install the required packages using `pip install -r requirements.txt`.
3. Copy '.env.example' to '.env' and fill in the required google API key.
4. Run the application using `python main.py`.

## Usage

This application will load the practitioner's address and additional addresses from the JSON files, create bookings for these addresses, and then calculate the optimal itinerary for visiting these addresses.

The itinerary is printed in the console. Each line represents a booking, displaying the booking id, the address id, the arrival and departure times, and the distance and duration from the previous address.


Example output:
```
python main.py
Remaining bookings:
5: 4
7: 6
8: 7
9: 8
10: 9
11: 10
13: 12
14: 13
23: 22
Optimal path:
1: 1 at 08:00 until 08:00                               # start
12: 11 at 08:08 until 08:38 after 4.478km and 00:08
4: 3 at 08:39 until 09:09 after 0.583km and 00:01
6: 5 at 09:15 until 09:45 after 2.239km and 00:05
15: 14 at 09:55 until 10:25 after 7.054km and 00:10
17: 16 at 10:33 until 11:03 after 6.361km and 00:07
18: 17 at 11:06 until 11:36 after 1.639km and 00:02
16: 15 at 11:37 until 12:07 after 0.231km and 00:00
20: 19 at 12:11 until 12:41 after 1.575km and 00:04
3: 1 at 13:00 until 15:00                               # fixed booking
21: 20 at 15:14 until 15:44 after 10.947km and 00:14
22: 21 at 15:47 until 16:17 after 2.114km and 00:03
24: 23 at 16:30 until 17:00 after 7.599km and 00:12
19: 18 at 17:06 until 17:36 after 3.688km and 00:06
2: 1 at 18:00 until 18:00                               # end
https://www.google.com/maps/dir/'16.235876,-61.5395697'/'16.2239845,-61.5261854'/'16.2206519,-61.5230288'/'16.2169304,-61.5129364'/'16.2581168,-61.5221207'/'16.2405353,-61.5547241'/'16.2376369,-61.5673074'/'16.2391914,-61.5670872'/'16.2195303,-61.565522'/'16.235876,-61.5395697'/'16.2413581,-61.612037'/'16.2295509,-61.6251799'/'16.2606482,-61.6504672'/'16.2364314,-61.6575426'/'16.235876,-61.5395697'?entry=ttu
```