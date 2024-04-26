#!/usr/bin/python3
'''
this script takes in a URL and displays the value of X-Request-Id
found in header of the response
'''
import urllib.request
import sys

url = sys.argv[1]
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    _id = response.headers.get('X-Request-Id')

print(_id)
