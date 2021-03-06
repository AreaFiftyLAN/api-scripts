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
seatgroup = input("What is the name of the seatgroup you want to add?\n")
seats = input("How many seats should this seatgroup contain?\n")
choice = input("Are you sure you want to add a seatgroup {} with {} seats? [Yes]: ".format(seatgroup, seats))
if choice =="Yes":
    print("Adding seatgroup")
    payload = {
            'seatGroupName': seatgroup,
            'numberOfSeats': seats
    }
    response = s.post(baseUrl + "/seats", json=payload)
    if response.json()["status"] == '200':
        print("Successfully added seatgroup")
    else:
        print(response.json())
else:
    print("Aborted adding a seatgroup")
