#!/usr/bin/python3
"""
Sends a request to a URL and displays the value of
the X-Request-Id variable in the header of the response
"""
import urllib.request
import sys


def get_x_request_id(url):
    with urllib.request.urlopen(url) as response:
        x_request_id = response.headers.get('X-Request-Id')
        return x_request_id


if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]
        x_request_id = get_x_request_id(url)
        print(x_request_id)
    else:
        print("Usage: ./1-hbtn_header.py <URL>")
