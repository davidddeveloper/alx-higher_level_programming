#!/usr/bin/python3
"""
    a Python script that takes your GitHub credentials
    (username and password)
    and uses the GitHub API to display your id
"""
import requests as re
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    passowrd = sys.argv[2]
    token = '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'

    headers = {
           'Accept': 'application/vnd.github+json',
           'Authorization': f'Bearer {token}',
           'X-GitHub-Api-Version': '2022-11-28'
    }
    r = re.get(url, headers=headers)
    json = r.json()

    print(json.get('id'))
