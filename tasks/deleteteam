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
team = input("What is the id of the team you want to delete?\n")
print(s.get(baseUrl + "/teams/{}".format(team)).json())
choice = input("Are you sure you want to delete team " + s.get(baseUrl + "/teams/{}".format(team)).json()["teamName"] + "? [Yes]: ")
if choice =="Yes":
    print("Deleting team")
    response = s.delete(baseUrl + "/teams/{}".format(team))
    if response.json()["status"] == '200':
        print("Successfully deleted")
    else:
        print(response.json())
else:
    print("Aborted team delete")
