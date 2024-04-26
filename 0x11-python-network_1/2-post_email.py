#!/usr/bin/python3
'''
this script takes in URL and sends a post request to it
it takes email as parameter and displays the decoded response

urllib.parse.urlencode - standard way of passing POST data
data.encode - type of encoding that you want on the data to send
'''

import urllib
import sys

url = sys.argv[1]
email = sys.argv[2]
data = urllib.parse.urlencode(email)
data = data.encode("utf-8")
req = urllib.request.Request(url, data)
with urllib.reuest.urlopen(req) as response:
    decode = response.decode('utf-8')
    html = response.read()
    print('Your email is: ', html)
