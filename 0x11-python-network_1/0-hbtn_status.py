#!/usr/bin/python3
'''
this script fetches: https://alx-intranet.hbtn.io/status
using urllib package
'''

import urllib.request

url = urllib.request.Request("https://alx-intranet.hbtn.io/status")
with urllib.request.urlopen(url) as response:
    html = response.read()

print("Body response:")
print("\t- type:", type(html))
print("\t- content:", html)
print("\t- utf8 content:", html.decode('utf-8'))
