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
Address                                              Arrival Time    Departure Time      Kms to reach  Time to reach
---------------------------------------------------  --------------  ----------------  --------------  ---------------
2 Rue Schoelcher, Pointe-Ã -Pitre 97110, Guadeloupe  08:00:00        08:00:00
Aquarium of Guadeloupe, Guadeloupe                   08:10:01        08:40:01                   5.151  00:10:01
Restaurant le Bordeaux, Guadeloupe                   08:54:30        09:24:30                  14.813  00:14:29
Caribbean Social Agency, Guadeloupe                  09:27:59        09:57:59                   2.114  00:03:29
Pharmacie la ROSIERE, Guadeloupe                     10:12:12        10:42:12                   8.819  00:14:13
Jardin Botanique de Deshaies, Guadeloupe             11:23:50        11:53:50                  31.168  00:41:38
St. Anne Market, Guadeloupe                          13:09:31        13:39:31                  62.722  01:15:41
2 Rue Schoelcher, Pointe-Ã -Pitre 97110, Guadeloupe  14:09:22        14:09:22                  21.83   00:29:51

Url: https://www.google.com/maps/dir/16.235876,-61.5395697/16.2206519,-61.5230288/16.2413581,-61.612037/16.2295509,-61.6251799/16.2406321,-61.6643745/16.2991842,-61.7976432/16.2242383,-61.3845464/16.235876,-61.5395697?entry=ttu


Tuesday
Address                                              Arrival Time    Departure Time      Kms to reach  Time to reach
---------------------------------------------------  --------------  ----------------  --------------  ---------------
2 Rue Schoelcher, Pointe-Ã -Pitre 97110, Guadeloupe  08:00:00        08:00:00
Sculpture artistique, Guadeloupe                     08:08:11        08:38:11                   4.478  00:08:11
Fort Fleur d'Ã‰pÃ©e, Guadeloupe                      08:43:36        09:13:36                   2.567  00:05:25
Restaurant Les Colibris, Guadeloupe                  09:23:57        09:53:57                   7.054  00:10:21
Le combava, Guadeloupe                               10:01:48        10:31:48                   6.361  00:07:51
Le Comptoir des Saveurs Jarry, Guadeloupe            10:34:27        11:04:27                   1.639  00:02:39
BUNBO, Guadeloupe                                    11:05:17        11:35:17                   0.231  00:00:50
2 Rue Schoelcher, Pointe-Ã -Pitre 97110, Guadeloupe  11:45:30        13:45:30                   5.837  00:10:13
La Cantina, Guadeloupe                               13:58:50        14:28:50                   7.227  00:13:20
L Exotic brefort Lamentin guadeloupe , Guadeloupe    14:47:10        15:17:10                  13.893  00:18:20
KARA tasty experiences, Guadeloupe                   15:23:51        15:53:51                   3.688  00:06:41
Cascade aux Ecrevisses, Guadeloupe                   16:06:01        16:36:01                   9.71   00:12:10
Museum costumes and traditions, Guadeloupe           17:05:09        17:35:09                  30.532  00:29:08
2 Rue Schoelcher, Pointe-Ã -Pitre 97110, Guadeloupe  17:50:33        17:50:33                  10.597  00:15:24

Url: https://www.google.com/maps/dir/16.235876,-61.5395697/16.2239845,-61.5261854/16.2169304,-61.5129364/16.2581168,-61.5221207/16.2405353,-61.5547241/16.2376369,-61.5673074/16.2391914,-61.5670872/16.235876,-61.5395697/16.2195303,-61.565522/16.2606482,-61.6504672/16.2364314,-61.6575426/16.1789129,-61.6809609/16.2097636,-61.4790638/16.235876,-61.5395697?entry=ttu


Wednesday
Address                                                           Arrival Time    Departure Time      Kms to reach  Time to reach
----------------------------------------------------------------  --------------  ----------------  --------------  ---------------
2 Rue Schoelcher, Pointe-Ã -Pitre 97110, Guadeloupe               08:00:00        08:00:00
Aquarium of Guadeloupe, Guadeloupe                                08:10:01        08:40:01                   5.151  00:10:01
Restaurant le Bordeaux, Guadeloupe                                08:54:30        09:24:30                  14.813  00:14:29
Caribbean Social Agency, Guadeloupe                               09:27:59        09:57:59                   2.114  00:03:29
Pharmacie la ROSIERE, Guadeloupe                                  10:12:12        10:42:12                   8.819  00:14:13
2 Rue Schoelcher, Pointe-Ã -Pitre 97110, Guadeloupe               11:02:35        13:02:35                  17.116  00:20:23
ECOMUSEE CREOLEART OF GUADELOUPE AND DREAMS OF VILLA, Guadeloupe  13:33:23        14:03:23                  25.089  00:30:48
Pointe AllÃ¨gre, Guadeloupe                                       14:18:20        14:48:20                   9.013  00:14:57
Plage de Grande Anse, Guadeloupe                                  15:02:57        15:32:57                   8.945  00:14:37
Jardin Botanique de Deshaies, Guadeloupe                          15:40:56        16:10:56                   3.841  00:07:59
2 Rue Schoelcher, Pointe-Ã -Pitre 97110, Guadeloupe               17:01:16        17:01:16                  41.805  00:50:20

Url: https://www.google.com/maps/dir/16.235876,-61.5395697/16.2206519,-61.5230288/16.2413581,-61.612037/16.2295509,-61.6251799/16.2406321,-61.6643745/16.235876,-61.5395697/16.3124734,-61.7054634/16.3617922,-61.7438846/16.3221395,-61.7886034/16.2991842,-61.7976432/16.235876,-61.5395697?entry=ttu


Thursday
Address                                              Arrival Time    Departure Time      Kms to reach  Time to reach
---------------------------------------------------  --------------  ----------------  --------------  ---------------
2 Rue Schoelcher, Pointe-Ã -Pitre 97110, Guadeloupe  08:00:00        08:00:00
Sculpture artistique, Guadeloupe                     08:08:11        08:38:11                   4.478  00:08:11
Fort Fleur d'Ã‰pÃ©e, Guadeloupe                      08:43:36        09:13:36                   2.567  00:05:25
Restaurant Les Colibris, Guadeloupe                  09:23:57        09:53:57                   7.054  00:10:21
Le combava, Guadeloupe                               10:01:48        10:31:48                   6.361  00:07:51
Le Comptoir des Saveurs Jarry, Guadeloupe            10:34:27        11:04:27                   1.639  00:02:39
BUNBO, Guadeloupe                                    11:05:17        11:35:17                   0.231  00:00:50
2 Rue Schoelcher, Pointe-Ã -Pitre 97110, Guadeloupe  11:45:30        13:45:30                   5.837  00:10:13
La Cantina, Guadeloupe                               13:58:50        14:28:50                   7.227  00:13:20
L Exotic brefort Lamentin guadeloupe , Guadeloupe    14:47:10        15:17:10                  13.893  00:18:20
KARA tasty experiences, Guadeloupe                   15:23:51        15:53:51                   3.688  00:06:41
Cascade aux Ecrevisses, Guadeloupe                   16:06:01        16:36:01                   9.71   00:12:10
Museum costumes and traditions, Guadeloupe           17:05:09        17:35:09                  30.532  00:29:08
2 Rue Schoelcher, Pointe-Ã -Pitre 97110, Guadeloupe  17:50:33        17:50:33                  10.597  00:15:24

Url: https://www.google.com/maps/dir/16.235876,-61.5395697/16.2239845,-61.5261854/16.2169304,-61.5129364/16.2581168,-61.5221207/16.2405353,-61.5547241/16.2376369,-61.5673074/16.2391914,-61.5670872/16.235876,-61.5395697/16.2195303,-61.565522/16.2606482,-61.6504672/16.2364314,-61.6575426/16.1789129,-61.6809609/16.2097636,-61.4790638/16.235876,-61.5395697?entry=ttu


Friday
Address                                                           Arrival Time    Departure Time      Kms to reach  Time to reach
----------------------------------------------------------------  --------------  ----------------  --------------  ---------------
2 Rue Schoelcher, Pointe-Ã -Pitre 97110, Guadeloupe               08:00:00        08:00:00
Aquarium of Guadeloupe, Guadeloupe                                08:10:01        08:40:01                   5.151  00:10:01
Restaurant le Bordeaux, Guadeloupe                                08:54:30        09:24:30                  14.813  00:14:29
Caribbean Social Agency, Guadeloupe                               09:27:59        09:57:59                   2.114  00:03:29
Pharmacie la ROSIERE, Guadeloupe                                  10:12:12        10:42:12                   8.819  00:14:13
2 Rue Schoelcher, Pointe-Ã -Pitre 97110, Guadeloupe               11:02:35        13:02:35                  17.116  00:20:23
ECOMUSEE CREOLEART OF GUADELOUPE AND DREAMS OF VILLA, Guadeloupe  13:33:23        14:03:23                  25.089  00:30:48
Pointe AllÃ¨gre, Guadeloupe                                       14:18:20        14:48:20                   9.013  00:14:57
Plage de Grande Anse, Guadeloupe                                  15:02:57        15:32:57                   8.945  00:14:37
Jardin Botanique de Deshaies, Guadeloupe                          15:40:56        16:10:56                   3.841  00:07:59
2 Rue Schoelcher, Pointe-Ã -Pitre 97110, Guadeloupe               17:01:16        17:01:16                  41.805  00:50:20

Url: https://www.google.com/maps/dir/16.235876,-61.5395697/16.2206519,-61.5230288/16.2413581,-61.612037/16.2295509,-61.6251799/16.2406321,-61.6643745/16.235876,-61.5395697/16.3124734,-61.7054634/16.3617922,-61.7438846/16.3221395,-61.7886034/16.2991842,-61.7976432/16.235876,-61.5395697?entry=ttu


Missed bookings:
Missed Address
---------------------------
Fort DelgrÃ¨s, Guadeloupe
St. Anne Market, Guadeloupe
Fort DelgrÃ¨s, Guadeloupe
St. Anne Market, Guadeloupe
Cached requests: 875
Api requests: 0

Process finished with exit code 0

```