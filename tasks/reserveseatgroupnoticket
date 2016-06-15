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
seatgroup = input("What is the name of the seatgroup you want to reserve?\n")
seats = input("What is the size of the group to reserve?\n")
choice = input("Are you sure you want to reserve seatgroup {} with {} seats? [Yes]: ".format(seatgroup, seats))
if choice =="Yes":
    print("Reserving seats")
    for x in range(1, int(seats) + 1):
        payload = {
                'group': seatgroup,
                'number': x
        }
        response = s.post(baseUrl + "/seats/reservations", json=payload)
        if response.json()["status"] == '200':
            print("Successfully reserved seat {} {}.".format(seatgroup, x))
        else:
            print(response.json())
else:
    print("Aborted reserving seatgroup")
