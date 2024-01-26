#!/usr/bin/python3
"""
Sends a request to a URL and displays the body of the response,
handling HTTPError exceptions
"""
import urllib.request
import urllib.error
import sys


def fetch_url_content(url):
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('utf-8')
            print(content)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]
        fetch_url_content(url)
    else:
        print("Usage: ./3-error_code.py <URL>")
