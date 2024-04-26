#!/usr/bin/python3
'''
this script takes in a URL and displays the value of X-Request-Id
found in header of the response
make sure to print the content inside the with block
it ensures the _id is the expected ID
'''
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        _id = response.headers.get('X-Request-Id')
        print(_id)
