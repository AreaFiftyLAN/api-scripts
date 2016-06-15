import os
import connection
import configparser

# Read config file
config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), "../config/config"))
baseUrl = config.get("Server", "Url")

# Sets up api connection
s = connection.connect()
# Send request to retrieve orders
seats = s.get(baseUrl + "/seats").json()['seatmap']
for group in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']:
    for seat in seats[group]:
        if (seat['taken']):
            if seat['ticket'] is not None and seat['ticket']['owner']['profile']['displayName'] is not None:
                print(seat['seatGroup'] + "," + str(seat['seatNumber']) + "," + seat['ticket']['owner']['profile']['displayName'])
