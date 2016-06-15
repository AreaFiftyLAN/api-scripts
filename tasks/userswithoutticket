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
mails = [ticket['owner']['email'] for ticket in tickets]
users = s.get(baseUrl + "/users").json()
for user in users:
    if not user['email'] in mails:
        print(user['email'])

