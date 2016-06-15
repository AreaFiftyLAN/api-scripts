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
ticket = input("What is the ticket id of the user you want to reserve the seat for?\n")
choice = input("Are you sure you want to reserve seat {} {} for ticketid {}? [Yes]: ".format(seatgroup, seat, ticket))
if choice =="Yes":
    print("Reserving seat")
    payload = {'ticketId': ticket}
    response = s.post(baseUrl + "/seats/{}/{}".format(seatgroup, seat, ticket), params=payload)
    if response.json()["status"] == '200':
        print("Successfully reserved seat {} {} for {}.".format(seatgroup, seat, ticket))
    else:
        print(response.json())
else:
    print("Aborted reserving seat")
