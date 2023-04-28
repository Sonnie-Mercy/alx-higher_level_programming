#!/usr/bin/python3
"""Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id"""

import sys
import requests

if __name__ == "__main__":
    user = "https://api.github.com/user", auth = (sys.argv[1], sys.argv[2])
    req = requests.get(user)
    content = req.json()
    print(content.get("id"))
