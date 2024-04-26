#!/usr/bin/python3
'''
this script fetches a url using the package request
'''
import requests


if __name__ == "__main__":
    r = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: ", type(r.text))
    print("\t- content: ", r.content)
