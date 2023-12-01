#!/usr/bin/python3
"""
Takes in a URL,
sends a request to the URL and displays
the body of the response (decoded in utf-8)
"""

if __name__ == "__main__":
    import urllib.request
    from urllib.error import HTTPError
    from sys import argv

    url = argv[1]

    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as http_ex:
        print("Error code: {}".format(http_ex.code))
