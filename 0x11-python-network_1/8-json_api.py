#!/usr/bin/python3
'''
Script takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user as a parameter
'''

import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"

    try:
        val = sys.argv[1]
    except IndexError:
        val = ""

    payload = {"q": val}
    req = requests.post(url, data=payload)
    try:
        Data = req.json()

        if Data:
            print("[{}] {}".format(Data['id'], Data['name']))
        else:
            print("No result")
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")
