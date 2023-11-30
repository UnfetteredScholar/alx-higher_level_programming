#!/bin/bash
# Displays all methods a server will accept for a URL
curl -sI -X "$1" | grep "Allow:" | sed -ne 's/^Allow: //p'
