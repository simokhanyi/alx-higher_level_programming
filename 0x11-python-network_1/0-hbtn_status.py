#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status using urllib
"""
import urllib.request


def fetch_status(url):
    with urllib.request.urlopen(url) as response:
        content = response.read()
    return content


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    content = fetch_status(url)

    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
    print("\t- utf8 content:", content.decode('utf-8'))
