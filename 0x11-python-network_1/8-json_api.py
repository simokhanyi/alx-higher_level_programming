#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""
import requests
import sys


def search_user(letter):
    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': letter}

    response = requests.post(url, data=data)

    try:
        result = response.json()
        if result:
            print("[{}] {}".format(result.get('id'), result.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        search_user("")
    else:
        search_user(sys.argv[1])
