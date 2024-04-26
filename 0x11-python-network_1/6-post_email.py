#!/usr/bin/python3
'''
sends a POST request to passed URL with email
displays the body response
'''

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    r = requests.post(url, data={"email": email})
    print(r.content)
