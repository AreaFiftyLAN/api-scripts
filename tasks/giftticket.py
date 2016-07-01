import os
import connection
import configparser

# Read config file
config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), "../config/config"))
baseUrl = config.get("Server", "Url")

# Sets up api connection
s = connection.connect()

# Gets input from the user
user = input("The ticket recipient: ")

pickupstring = input("Should the ticket have pickup? [Yes]: ")
if pickupstring == "Yes":
    pickup = True
else:
    pickup = False

chmemberstring = input("Is the owner a discount member? [Yes]: ")
if chmemberstring == "Yes":
    chmember = True
else:
    chmember = False

choice = input("Are you sure you want to gift a ticket to user {} with options [pickup: {}, chmember:{}]? [Yes]: ".format(user, pickup, chmember))
if choice == "Yes":
    data = {
        "pickupService": pickup,
        "chMember": chmember,
        "type": "FREE"
    }
    order = s.post(baseUrl + "/users/{}/orders".format(user) , json=data)
    response = s.post(baseUrl + "/orders/{}/approve".format(order.json()["object"]["id"]))
    if response.json()["status"] == '200':
        print("Successfully gifted ticket to user {} with options [pickup: {}, chmember:{}].".format(user, pickup, chmember))
    else:
        print(response.json())
else:
    print("Aborted action")
