#!/usr/bin/python3
'''
this scripts senda a requrst to passed URL
displays the value of variable X-Request-Id
'''

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)

    print(req.headers.get('X-Request-Id'))
