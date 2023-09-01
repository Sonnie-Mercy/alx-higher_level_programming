#!/usr/bin/python3
"""takes URL, sends request to URL, displays body of response
manages urllib.error.HTTPError exceptions"""
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPerror as e:
        print("Error code:", e.code)
