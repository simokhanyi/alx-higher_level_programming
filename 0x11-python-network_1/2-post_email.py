#!/usr/bin/python3
"""
Sends a POST request to a URL with an email parameter
and displays the body of the response
"""
import urllib.request
import urllib.parse
import sys


def post_email(url, email):
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')

    with urllib.request.urlopen(req) as response:
        content = response.read().decode('utf-8')
        print(content)


if __name__ == "__main__":
    if len(sys.argv) == 3:
        url = sys.argv[1]
        email = sys.argv[2]
        post_email(url, email)
    else:
        print("Usage: ./2-post_email.py <URL> <email>")
