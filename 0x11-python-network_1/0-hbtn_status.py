#!/usr/bin/python3
"""a Python script that fetches https://alx-intranet.hbtn.io/status"""

import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
with urllib.request.urlopen(url) as response:
    content = response.read()
    print("- type: {}".format(type(content)))
    print("- content: {}".format(content))
    print("- utf8 content: {}".format(content.decode('utf-8')))
