#!/bin/bash
# Send a post request with a JSON body
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
