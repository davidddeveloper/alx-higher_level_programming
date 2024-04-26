"""
a Python script that fetches
'https://alx-intranet.hbtn.io/status'

"""
import urllib.request as re


url = 'https://alx-intranet.hbtn.io/status'
with re.urlopen(url) as response:
  print(response.read())
