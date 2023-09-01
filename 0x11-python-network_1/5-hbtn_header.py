#!/usr/bin/python3
"""using requests instead of urllib"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        response = requests.get(url)
        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id:
            print(x_request_id)
    except Exception as e:
        print(e)
