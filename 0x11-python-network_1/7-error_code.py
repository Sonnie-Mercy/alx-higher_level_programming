#!/usr/bin/python3
"""more use of the requests library"""
import requests
import sys

url = sys.argv[1]

try:
    response = requests.get(url)
    print(response.text)

    if response.status_code >= 400:
        print("Error code:", response.status_code)
except Exception as e:
    print(e)
