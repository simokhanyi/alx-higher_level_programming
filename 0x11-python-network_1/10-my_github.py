#!/usr/bin/python3
"""
Uses the GitHub API to display the user id using Basic Authentication
"""
import requests
import sys


def get_github_user_id(username, password):
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, password))

    try:
        user_data = response.json()
        user_id = user_data.get('id')
        return user_id
    except ValueError:
        return None


if __name__ == "__main__":
    if len(sys.argv) == 3:
        username = sys.argv[1]
        password = sys.argv[2]
        result = get_github_user_id(username, password)
        print(result)
    else:
        print("Usage: ./10-my_github.py <username> <password>")
