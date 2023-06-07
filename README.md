# Python Booking Scheduler

Python Booking Scheduler

Python Booking Scheduler is a Python application that simulates scheduling and path finding for a range of appointments, generating an itinerary for a practitioner to visit different addresses in a week. This system leverages the Google Maps API for route optimization.

## Features
- Load practitioner and address data from JSON files.
- Create fake booking scenarios for demonstration purposes.
- Use the Google Maps API to find optimal paths between bookings.
- Generate a weekly plan in an easy-to-read tabular format.
- Identify missed bookings and list them separately.
- Caches requests to reduce Google Maps API calls.

## Setup
Prerequisites:
- Python 3.11
- Google Maps Directions API key

## Installation
1. Clone the repository.
2. Install the required packages using `pip install -r requirements.txt`.
3. Copy '.env.example' to '.env' and fill in the required google API key.
4. Run the application using `python main.py`.

## Output

The output of the program is a weekly schedule with daily routes and a link to a Google Maps itinerary for each day. Missed bookings are displayed at the end of the output, along with the counts of cached and actual API requests to Google Maps API.

### Example:
```
python main.py

Monday
Address                                              Arrival Time    Booking Time    Departure Time      Kms to reach  Time to reach    Free Time Before Booking
---------------------------------------------------  --------------  --------------  ----------------  --------------  ---------------  --------------------------
2 Rue Schoelcher, Pointe-Ã -Pitre 97110, Guadeloupe                  08:00:00        08:00:00
Sculpture artistique, Guadeloupe                     08:08:11        08:08:11        08:38:11                   4.478  00:08:11
Aquarium of Guadeloupe, Guadeloupe                   08:39:48        08:39:48        09:09:48                   0.583  00:01:37
Fort Fleur d'Ã‰pÃ©e, Guadeloupe                      09:15:25        09:15:25        09:45:25                   2.239  00:05:37
Restaurant Les Colibris, Guadeloupe                  09:55:46        09:55:46        10:25:46                   7.054  00:10:21
BUNBO, Guadeloupe                                    10:36:10        10:36:10        11:06:10                   7.628  00:10:24
La Cantina, Guadeloupe                               11:10:14        11:10:14        11:40:14                   1.575  00:04:04
2 Rue Schoelcher, Pointe-Ã -Pitre 97110, Guadeloupe  11:52:15        12:00:00        14:00:00                   6.26   00:12:01         00:07:45
Caribbean Social Agency, Guadeloupe                  14:18:24        14:18:24        14:48:24                  14.795  00:18:24
L Exotic brefort Lamentin guadeloupe , Guadeloupe    15:00:39        15:00:39        15:30:39                   7.599  00:12:15
KARA tasty experiences, Guadeloupe                   15:37:20        15:37:20        16:07:20                   3.688  00:06:41
Cascade aux Ecrevisses, Guadeloupe                   16:19:30        16:19:30        16:49:30                   9.71   00:12:10
2 Rue Schoelcher, Pointe-Ã -Pitre 97110, Guadeloupe  17:12:13        18:00:00        18:00:00                  21.878  00:22:43         00:47:47

Url: https://www.google.com/maps/dir/16.235876,-61.5395697/16.2239845,-61.5261854/16.2206519,-61.5230288/16.2169304,-61.5129364/16.2581168,-61.5221207/16.2391914,-61.5670872/16.2195303,-61.565522/16.235876,-61.5395697/16.2295509,-61.6251799/16.2606482,-61.6504672/16.2364314,-61.6575426/16.1789129,-61.6809609/16.235876,-61.5395697?entry=ttu


Tuesday
Address                                                           Arrival Time    Booking Time    Departure Time      Kms to reach  Time to reach    Free Time Before Booking
----------------------------------------------------------------  --------------  --------------  ----------------  --------------  ---------------  --------------------------
2 Rue Schoelcher, Pointe-Ã -Pitre 97110, Guadeloupe                               08:00:00        08:00:00
Le combava, Guadeloupe                                            08:09:28        08:09:28        08:39:28                   5.523  00:09:28
Le Comptoir des Saveurs Jarry, Guadeloupe                         08:42:07        08:42:07        09:12:07                   1.639  00:02:39
Restaurant le Bordeaux, Guadeloupe                                09:20:14        09:20:14        09:50:14                   5.159  00:08:07
Pharmacie la ROSIERE, Guadeloupe                                  10:04:00        10:04:00        10:34:00                  11.381  00:13:46
ECOMUSEE CREOLEART OF GUADELOUPE AND DREAMS OF VILLA, Guadeloupe  10:53:44        10:53:44        11:23:44                  13.708  00:19:44
2 Rue Schoelcher, Pointe-Ã -Pitre 97110, Guadeloupe               11:53:15        12:00:00        14:00:00                  24.419  00:29:31         00:06:45
Museum costumes and traditions, Guadeloupe                        14:15:11        14:15:11        14:45:11                  10.328  00:15:11
St. Anne Market, Guadeloupe                                       15:07:05        15:07:05        15:37:05                  13.226  00:21:54
Pointe AllÃ¨gre, Guadeloupe                                       16:38:29        16:38:29        17:08:29                  50.918  01:01:24
2 Rue Schoelcher, Pointe-Ã -Pitre 97110, Guadeloupe               17:49:33        18:00:00        18:00:00                  31.024  00:41:04         00:10:27

Url: https://www.google.com/maps/dir/16.235876,-61.5395697/16.2405353,-61.5547241/16.2376369,-61.5673074/16.2413581,-61.612037/16.2406321,-61.6643745/16.3124734,-61.7054634/16.235876,-61.5395697/16.2097636,-61.4790638/16.2242383,-61.3845464/16.3617922,-61.7438846/16.235876,-61.5395697?entry=ttu


Wednesday
Address                                              Arrival Time    Booking Time    Departure Time      Kms to reach  Time to reach    Free Time Before Booking
---------------------------------------------------  --------------  --------------  ----------------  --------------  ---------------  --------------------------
2 Rue Schoelcher, Pointe-Ã -Pitre 97110, Guadeloupe                  08:00:00        08:00:00
Sculpture artistique, Guadeloupe                     08:08:11        08:08:11        08:38:11                   4.478  00:08:11
Aquarium of Guadeloupe, Guadeloupe                   08:39:48        08:39:48        09:09:48                   0.583  00:01:37
Fort Fleur d'Ã‰pÃ©e, Guadeloupe                      09:15:25        09:15:25        09:45:25                   2.239  00:05:37
Restaurant Les Colibris, Guadeloupe                  09:55:46        09:55:46        10:25:46                   7.054  00:10:21
BUNBO, Guadeloupe                                    10:36:10        10:36:10        11:06:10                   7.628  00:10:24
La Cantina, Guadeloupe                               11:10:14        11:10:14        11:40:14                   1.575  00:04:04
2 Rue Schoelcher, Pointe-Ã -Pitre 97110, Guadeloupe  11:52:15        12:00:00        14:00:00                   6.26   00:12:01         00:07:45
Caribbean Social Agency, Guadeloupe                  14:18:24        14:18:24        14:48:24                  14.795  00:18:24
L Exotic brefort Lamentin guadeloupe , Guadeloupe    15:00:39        15:00:39        15:30:39                   7.599  00:12:15
KARA tasty experiences, Guadeloupe                   15:37:20        15:37:20        16:07:20                   3.688  00:06:41
Cascade aux Ecrevisses, Guadeloupe                   16:19:30        16:19:30        16:49:30                   9.71   00:12:10
2 Rue Schoelcher, Pointe-Ã -Pitre 97110, Guadeloupe  17:12:13        18:00:00        18:00:00                  21.878  00:22:43         00:47:47

Url: https://www.google.com/maps/dir/16.235876,-61.5395697/16.2239845,-61.5261854/16.2206519,-61.5230288/16.2169304,-61.5129364/16.2581168,-61.5221207/16.2391914,-61.5670872/16.2195303,-61.565522/16.235876,-61.5395697/16.2295509,-61.6251799/16.2606482,-61.6504672/16.2364314,-61.6575426/16.1789129,-61.6809609/16.235876,-61.5395697?entry=ttu


Thursday
Address                                                           Arrival Time    Booking Time    Departure Time      Kms to reach  Time to reach    Free Time Before Booking
----------------------------------------------------------------  --------------  --------------  ----------------  --------------  ---------------  --------------------------
2 Rue Schoelcher, Pointe-Ã -Pitre 97110, Guadeloupe                               08:00:00        08:00:00
Le combava, Guadeloupe                                            08:09:28        08:09:28        08:39:28                   5.523  00:09:28
Le Comptoir des Saveurs Jarry, Guadeloupe                         08:42:07        08:42:07        09:12:07                   1.639  00:02:39
Restaurant le Bordeaux, Guadeloupe                                09:20:14        09:20:14        09:50:14                   5.159  00:08:07
Pharmacie la ROSIERE, Guadeloupe                                  10:04:00        10:04:00        10:34:00                  11.381  00:13:46
ECOMUSEE CREOLEART OF GUADELOUPE AND DREAMS OF VILLA, Guadeloupe  10:53:44        10:53:44        11:23:44                  13.708  00:19:44
2 Rue Schoelcher, Pointe-Ã -Pitre 97110, Guadeloupe               11:53:15        12:00:00        14:00:00                  24.419  00:29:31         00:06:45
Museum costumes and traditions, Guadeloupe                        14:15:11        14:15:11        14:45:11                  10.328  00:15:11
St. Anne Market, Guadeloupe                                       15:07:05        15:07:05        15:37:05                  13.226  00:21:54
Pointe AllÃ¨gre, Guadeloupe                                       16:38:29        16:38:29        17:08:29                  50.918  01:01:24
2 Rue Schoelcher, Pointe-Ã -Pitre 97110, Guadeloupe               17:49:33        18:00:00        18:00:00                  31.024  00:41:04         00:10:27

Url: https://www.google.com/maps/dir/16.235876,-61.5395697/16.2405353,-61.5547241/16.2376369,-61.5673074/16.2413581,-61.612037/16.2406321,-61.6643745/16.3124734,-61.7054634/16.235876,-61.5395697/16.2097636,-61.4790638/16.2242383,-61.3845464/16.3617922,-61.7438846/16.235876,-61.5395697?entry=ttu


Friday
Address                                              Arrival Time    Booking Time    Departure Time      Kms to reach  Time to reach    Free Time Before Booking
---------------------------------------------------  --------------  --------------  ----------------  --------------  ---------------  --------------------------
2 Rue Schoelcher, Pointe-Ã -Pitre 97110, Guadeloupe                  08:00:00        08:00:00
Sculpture artistique, Guadeloupe                     08:08:11        08:08:11        08:38:11                   4.478  00:08:11
Aquarium of Guadeloupe, Guadeloupe                   08:39:48        08:39:48        09:09:48                   0.583  00:01:37
Fort Fleur d'Ã‰pÃ©e, Guadeloupe                      09:15:25        09:15:25        09:45:25                   2.239  00:05:37
Restaurant Les Colibris, Guadeloupe                  09:55:46        09:55:46        10:25:46                   7.054  00:10:21
BUNBO, Guadeloupe                                    10:36:10        10:36:10        11:06:10                   7.628  00:10:24
La Cantina, Guadeloupe                               11:10:14        11:10:14        11:40:14                   1.575  00:04:04
2 Rue Schoelcher, Pointe-Ã -Pitre 97110, Guadeloupe  11:52:15        12:00:00        14:00:00                   6.26   00:12:01         00:07:45
Caribbean Social Agency, Guadeloupe                  14:18:24        14:18:24        14:48:24                  14.795  00:18:24
L Exotic brefort Lamentin guadeloupe , Guadeloupe    15:00:39        15:00:39        15:30:39                   7.599  00:12:15
KARA tasty experiences, Guadeloupe                   15:37:20        15:37:20        16:07:20                   3.688  00:06:41
Cascade aux Ecrevisses, Guadeloupe                   16:19:30        16:19:30        16:49:30                   9.71   00:12:10
2 Rue Schoelcher, Pointe-Ã -Pitre 97110, Guadeloupe  17:12:13        18:00:00        18:00:00                  21.878  00:22:43         00:47:47

Url: https://www.google.com/maps/dir/16.235876,-61.5395697/16.2239845,-61.5261854/16.2206519,-61.5230288/16.2169304,-61.5129364/16.2581168,-61.5221207/16.2391914,-61.5670872/16.2195303,-61.565522/16.235876,-61.5395697/16.2295509,-61.6251799/16.2606482,-61.6504672/16.2364314,-61.6575426/16.1789129,-61.6809609/16.235876,-61.5395697?entry=ttu


Missed bookings:
Missed Address
----------------------------------------
Fort DelgrÃ¨s, Guadeloupe
Jardin Botanique de Deshaies, Guadeloupe
Plage de Grande Anse, Guadeloupe
Fort DelgrÃ¨s, Guadeloupe
Jardin Botanique de Deshaies, Guadeloupe
Plage de Grande Anse, Guadeloupe
Fort DelgrÃ¨s, Guadeloupe
Pointe AllÃ¨gre, Guadeloupe

Cached requests: 1060
Api requests: 0

```