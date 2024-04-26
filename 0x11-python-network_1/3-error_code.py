#!/usr/bin/python3
'''
this script takes in URL, sends a request to the URL
display the response(decode: utf-8)
Handle the HTTPError exceptions and print the Error code
'''

import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        try:
            html = response.read().decode('utf-8')
            print(html)
        except urllib.error.HTTPError as e:
            e_code = e.code
            print("Error code: ", e_code)
