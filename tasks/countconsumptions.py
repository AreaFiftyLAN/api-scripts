import os
import configparser
import json
import connection

# Read config file
config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), "../config/config"))
baseUrl = config.get("Server", "Url")

# Open connection
server = connection.connect()

# Parse Ticket IDs
ticket_ids = []
tickets = server.get(baseUrl + "/tickets").json()
for ticket in tickets:
    ticket_ids.append(ticket['id'])

# Parse Consumption names
consumption_names = []
consumptions = server.get(baseUrl + "/consumptions").json()
for consumption in consumptions:
    consumption_names.append(consumption['name'])

# Fill Dict
consumption_count = {}
for consumption_name in consumption_names:
    consumption_count[consumption_name] = 0

print("Please be patient, this might take a while.")

# Count consumptions per ticket
for ticket_id in ticket_ids:
    ticket_consumptions = server.get(baseUrl + "/consumptions/" + str(ticket_id)).json()
    for ticket_consumption in ticket_consumptions:
        consumption_count[ticket_consumption['name']] += 1

print(json.dumps(consumption_count, indent=4, sort_keys=True))
