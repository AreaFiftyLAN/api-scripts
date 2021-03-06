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
tickets = s.get(baseUrl + "/tickets").json()
for ticket in tickets:
    if (ticket['valid']):
#        print(ticket['owner']['username'] + ', ' + ticket['owner']['email'])
        print(ticket['owner']['username'])

