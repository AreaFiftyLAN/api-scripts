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
[print("{}, {}, {}".format(order["user"]["username"], len(order["tickets"]))) for order in orders.json()]
