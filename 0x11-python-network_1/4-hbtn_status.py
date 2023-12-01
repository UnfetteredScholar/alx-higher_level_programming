#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status
using the requests package
"""


if __name__ == "__main__":
    import requests

    url = "https://alx-intranet.hbtn.io/status"

    res = requests.get(url).text

    print("Body response:")
    print(f"\t- type: {type(res)}")
    print(f"\t- content: {res}")
