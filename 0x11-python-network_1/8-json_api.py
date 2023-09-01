#!/usr/bin/python3
"""takes a letter and sends POST request with letter as parameter"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    try:
        response = requests.post("http://0.0.0.0:5000/search_user", data={'q': q})
        data = response.json()

        if data:
            print("[{}] {}".format(data['id'], data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
    except Exception as e:
        print(e)
