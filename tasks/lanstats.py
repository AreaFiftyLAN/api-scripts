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
orders = s.get(baseUrl + "/orders")
tickets = sum(map(lambda x: len(x["tickets"]) if x['status'] == 'PAID' else 0, orders.json()))
print("Tickets: {}".format(tickets))
users = len(s.get(baseUrl + "/users").json())
print("Users: {}".format(users))
teams = len(s.get(baseUrl + "/teams").json())
print("Teams: {}".format(teams))
seats = s.get(baseUrl + "/seats").json()['seatmap']
reserved = 0
claimed = 0
for group in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']:
    for seat in seats[group]:
        if seat["taken"]:
            reserved += 1
        if seat["ticket"] != None:
            claimed += 1
print("Seats reserved: {}".format(reserved))
print("Seats claimed: {}".format(claimed))
