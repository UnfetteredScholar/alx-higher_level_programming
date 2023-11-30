#!/bin/bash
# Sends a get request with header variable X-School-User-Id=98 and displays the response body
curl -sL -H 'X-School-User-Id: 98' "$1"
