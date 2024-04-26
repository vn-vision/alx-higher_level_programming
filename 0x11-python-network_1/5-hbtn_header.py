#!/usr/bin/python3
'''
this scripts senda a requrst to passed URL
displays the value of variable X-Request-Id
'''

import requests
import sys

url = sys.argv[1]
req = requests.get(url)

print(req.headers['X-Request-Id'])
