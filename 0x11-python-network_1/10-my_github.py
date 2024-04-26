#!/usr/bin/python3
'''
Script takes in username and password and sends it GitHub API
display your ID
'''

import requests
import sys

if __name__ == "__main__":
    url = "https://api.github.com/user"

    USER = sys.argv[1]
    PASS = sys.argv[2]

    payload = {"username": USER, "password": PASS}

    # pass the username and passwords for authentication
    req = requests.post(url, data=payload, auth=(USER, PASS))

    # check for status code 200
    if req.status_code == 200:
        print(req.json()['id'])
    else:
        print("Failed to authenticate: ", req.status_code)
