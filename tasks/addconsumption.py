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
consumption = input("What is the name of the new consumption?\n")
choice = input("Are you sure you want to add a consumption with the name {}? [Yes]: ".format(consumption))
if choice =="Yes":
    print("Adding consumption")
    response = s.post(baseUrl + "/consumptions", data=consumption)
    if response.json()["status"] == '200':
        print("Successfully added consumption {}".format(consumption))
    else:
        print(response.json())
else:
    print("Aborted adding consumption")
