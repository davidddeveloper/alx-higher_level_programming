#!/usr/bin/python3
"""
    a Python script that fetches
    https://alx-intranet.hbtn.io/status
"""
import requests as re


if __name__ == "__main__":
    r = re.get('https://alx-intranet.hbtn.io/status')
    body = r.text

    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
