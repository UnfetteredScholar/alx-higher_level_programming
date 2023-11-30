#!/bin/bash
# Sends a post request to the passed url and displays the response body
curl -s -X 'POST' -d 'email=test@gmail.com&subject=I will always be here for PLD' "$1"
