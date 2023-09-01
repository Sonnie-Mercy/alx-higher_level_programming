#!/usr/bin/python3
"""taskes URL, sends request to URL and displays
the X-Request-ID found in the header"""
import urllib.request
import sys

url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    Id = response.getheader('X-Request-Id')
    if Id:
        print(Id)
