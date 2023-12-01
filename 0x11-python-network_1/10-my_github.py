#!/usr/bin/python3
"""
Takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

if __name__ == "__main__":
    import requests
    from requests.auth import HTTPBasicAuth
    from sys import argv

    endpoint = f"https://api.github.com/user"
    basic_auth = HTTPBasicAuth(argv[1], argv[2])

    response = requests.get(endpoint, auth=basic_auth).json()
    print(response.get('id'))
