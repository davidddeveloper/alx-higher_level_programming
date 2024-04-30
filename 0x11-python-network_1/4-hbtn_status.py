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
    print("    - type: {}".format(type(body)))
    print("    - content: {}".format(body))
