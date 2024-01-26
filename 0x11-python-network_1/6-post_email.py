#!/usr/bin/python3
"""
Sends a POST request to a URL with an email parameter
and displays the body of the response
"""
import requests
import sys


def post_email(url, email):
    payload = {'email': email}
    response = requests.post(url, data=payload)
    print(response.text)


if __name__ == "__main__":
    if len(sys.argv) == 3:
        url = sys.argv[1]
        email = sys.argv[2]
        post_email(url, email)
    else:
        print("Usage: ./6-post_email.py <URL> <email>")
