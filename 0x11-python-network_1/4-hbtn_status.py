#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status using the requests package
"""
import requests


def fetch_status(url):
    response = requests.get(url)
    return response.text


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    content = fetch_status(url)

    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
