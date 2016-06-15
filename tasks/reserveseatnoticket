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
seat = input("What is the seat number to reserve?\n")
choice = input("Are you sure you want to reserve seat {} {}? [Yes]: ".format(seatgroup, seat))
if choice =="Yes":
    print("Reserving seat")
    payload = {
            'group': seatgroup,
            'number': seat
    }
    response = s.post(baseUrl + "/seats/reservations", json=payload)
    if response.json()["status"] == '200':
        print("Successfully reserved seat {} {}.".format(seatgroup, seat))
    else:
        print(response.json())
else:
    print("Aborted reserving seat")
