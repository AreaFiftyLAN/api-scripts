#!/usr/bin/python3.5
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

    # Get the token from the server
    r = s.get(baseUrl + "/token")
    token = r.headers['X-CSRF-TOKEN']
    header = {
        'X-CSRF-TOKEN': token
    }
    s.headers.update(header)
    # Url parameters
    payload = {
            'username': username,
            'password': password
    }
    l = s.post(baseUrl + "/login", params=payload)
    newToken = s.get(baseUrl + "/token").headers["X-CSRF-TOKEN"]
    afterLoginHeader = {
        'X-CSRF-TOKEN': newToken
    }
    s.headers.update(afterLoginHeader)
    return s
