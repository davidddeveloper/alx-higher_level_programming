#!/usr/bin/python3
"""
    a Python script that takes in a letter and
    sends a POST request to http://0.0.0.0:5000/search_user
    with the letter as a parameter.
"""
import requests as re
import sys


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'

    try: q = sys.argv[1]
    except Exception:
        q = ""

    r = re.post(url, data={'q': q})
    json = r.json()

    if json == {}:
        print("No result")
    else:
        print(f"[{json['id']}] {json['name']}")
