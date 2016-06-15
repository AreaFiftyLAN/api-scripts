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
choice = input("Are you sure you want to add all seatgroups? [Yes]")
if choice == "Yes":
    print("Adding all seatgroups")
    for group in ['A', 'B', 'C', 'D', 'E']:
        seats = 16
        payload = {
                'seatGroupName': group,
                'numberOfSeats': seats
        }
        print(payload)
        response = s.post(baseUrl + "/seats", json=payload)
        if response.json()["status"] == '200':
            print("Successfully added seatgroup {} with {} seats.".format(group, seats))
        else:
            print(response.json())
    for group in ['F', 'G', 'H', 'I', 'J']:
        seats = 24
        payload = {
                'seatGroupName': group,
                'numberOfSeats': seats
        }
        response = s.post(baseUrl + "/seats", json=payload)
        if response.json()["status"] == '200':
            print("Successfully added seatgroup {} with {} seats.".format(group, seats))
        else:
            print(response.json())
else:
    print("Aborted adding a seatgroup")
