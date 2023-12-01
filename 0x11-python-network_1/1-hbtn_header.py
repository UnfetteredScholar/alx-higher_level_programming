#!/usr/bin/python3
"""Sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response."""
import urllib.request
from sys import argv

url = argv[1]
request = urllib.request.Request(url)

with urllib.request.urlopen(request) as response:
    print(response.headers['X-Request-Id'])
