#!/usr/bin/python3
"""takes username and password and uses GithubAPI to show ID"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"

    try:
        response = requests.get(url, auth=(username, password))
        if response.status_code == 200:
            data = response.json()
            print(data.get("id"))
        else:
            print(None)
    except Exception as e:
        print(None)
