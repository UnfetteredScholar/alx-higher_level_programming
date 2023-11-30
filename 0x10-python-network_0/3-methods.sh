#!/bin/bash
# Displays all methods a server will accept for a URL
curl -sI -X "OPTIONS" "$1" | grep -i "allow:" | sed 's/Allow: //'
