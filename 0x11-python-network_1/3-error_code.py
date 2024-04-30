#!/usr/bin/python3
"""
    a Python script that takes in a URL,
    sends a request to the URL and
    displays the body of the response (decoded in utf-8)
"""
import urllib.error as error
import urllib.request as re
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    req = re.Request(url)
    try:
        with re.urlopen(req) as response:
            res = response.read()
            print(res.decode('utf-8'))

    except error.HTTPError as e:
        print("Error code:", e.code)
