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
tickets = s.get(baseUrl + "/tickets/transport").json()
for ticket in tickets:
        profile = ticket['owner']['profile']
        print(profile['firstName'] + ',' + profile['lastName'] + ',' + profile['address'] + ',' + profile['city'] + ',' + profile['zipcode'] + ',' + profile['phoneNumber'] + ',' + ticket['owner']['username'])

