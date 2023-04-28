#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""

import urllib.error
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            cont = response.read().decode('utf-8')
            print(cont)

    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
