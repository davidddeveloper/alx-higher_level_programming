#!/usr/bin/python3
"""
a Python script that fetches
'https://alx-intranet.hbtn.io/status'

"""
import urllib.request as re


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    req = re.Request(url)

    with re.urlopen(req) as res:
        body = res.read()

        print('Body response:')
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
