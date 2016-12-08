import os
import configparser
import requests
import json

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), "../config/config"))

baseUrl = config.get("Server", "url")
username = config.get("Credentials", "username")
password = config.get("Credentials", "password")

def connect():
    # Use session for persistent headers
    s = requests.Session()

    # Url parameters
    payload = {
            'username': username,
            'password': password
    }
    l = s.post(baseUrl + '/token', json=payload)

    token = l.json()['object']
    header = {
        'X-Auth-Token': token
    }
    s.headers.update(header)
    return s
