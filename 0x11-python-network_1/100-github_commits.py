#!/usr/bin/python3
"""
Fetches the 10 most recent commits from a
GitHub repository using the GitHub API
"""
import requests
import sys


def fetch_github_commits(repo, owner):
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    params = {'per_page': 10}

    response = requests.get(url, params=params)

    try:
        commits = response.json()
        for commit in commits:
            sha = commit.get('sha')
            author_name = commit.get('commit',
                    {}).get('author', {}).get('name') or 'Unknown'
            print(f"{sha}: {author_name}")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    if len(sys.argv) == 3:
        repo = sys.argv[1]
        owner = sys.argv[2]
        fetch_github_commits(repo, owner)
    else:
        print("Usage: ./100-github_commits.py <repository> <owner>")
