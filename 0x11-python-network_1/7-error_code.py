#!/usr/bin/python3
'''
send a request to passed URL and displays the body of response
usage ./file <url>
returns the error code
'''

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)

    status_code = req.status_code

    if status_code >= 400:
        print("Error code:{}".format(status_code))
    else:
        print(req.text)
