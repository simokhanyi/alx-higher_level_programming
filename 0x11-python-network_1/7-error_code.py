#!/usr/bin/python3
"""
Sends a request to a URL and displays the body of the response,
handling HTTP errors
"""
import requests
import sys


def fetch_url_content(url):
    response = requests.get(url)
    print(response.text)

    if response.status_code >= 400:
        print("Error code:", response.status_code)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]
        fetch_url_content(url)
    else:
        print("Usage: ./7-error_code.py <URL>")
