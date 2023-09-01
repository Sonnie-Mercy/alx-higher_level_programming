#!/usr/bin/python3
"""Using email and a POST request using the requests library"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    try:
        response = requests.post(url, data={'email': email})
        print("Your email is:", email)
        print(response.text)
    except Exception as e:
        print(e)
