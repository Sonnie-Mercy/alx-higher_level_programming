#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status using requests only"""
import requests

url = 'https://alx-intranet.hbtn.io/status'

response = requests.get(url)

print("Body response:")
print("\t- type:", type(response.text))
print("\t- content:", response.text)
