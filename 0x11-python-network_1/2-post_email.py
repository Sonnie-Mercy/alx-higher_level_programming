#!/usr/bin/python3
""" Takes URL and email, sends POST request to URL with email as parameter
displays the body of the response in utf-8"""
import urllib.request
import urllib.parse
import sys

url = sys.argv[1]
email = sys.argv[2]

data = urllib.parse.urlencode({'email': email}).encode('utf-8')
req = urllib.request.Request(url, data=data, method='POST')
with urllib.request.urlopen(req) as response:
    body = response.read().decode('utf-8')
    print(body)
