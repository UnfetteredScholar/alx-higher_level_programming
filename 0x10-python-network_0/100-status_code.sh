#!/bin/bash
# Displays the status code of a respone
curl -so /dev/null --write-out "%{http_code}" "$1"
