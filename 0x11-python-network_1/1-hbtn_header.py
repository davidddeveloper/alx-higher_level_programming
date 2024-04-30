#!/usr/bin/python3
"""
    a Python script that takes in a URL,
    sends a request to the URL and displays the value of the
    X-Request-Id variable found in the header of the response

"""


import urllib.request as re
import sys

url = sys.argv[1]
with re.urlopen(url) as response:
    xRequestId = response.headers.get("X-Request-Id")
    print(xRequestId)
