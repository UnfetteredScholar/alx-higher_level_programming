#!/usr/bin/python3
"""
Lists 10 commits (from the most recent to oldest) of
the repository “rails” by the user “rails”
"""

if __name__ == "__main__":
    import requests
    from sys import argv
    url = f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits"

    commits = requests.get(url).json()
    count = 0
    for commit in commits:
        sha = commit.get('sha')
        name = commit.get('commit').get('author').get('name')
        print(f"{sha}: {name}")
        count += 1
        if count == 10:
            break
