#!/usr/bin/env python3
"""
Sends a request to a URL and displays the value of the X-Request-Id variable
in the response header.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    print(requests.get(url).headers.get('X-Request-Id'))
