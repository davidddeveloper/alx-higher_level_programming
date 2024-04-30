#!/usr/bin/python3
"""
    a Python script that takes in a URL and an email,
    sends a POST request to the passed URL with the email
    as a parameter,
    and displays the body of the response
"""
import urllib
import urllib.request as re
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}
    data = urllib.parse.urlencode(data)
    data = data.encode('ascii')

    req = re.Request(url, data)
    with re.urlopen(req) as response:
        res = response.read().decode('utf-8')
        print(res)
