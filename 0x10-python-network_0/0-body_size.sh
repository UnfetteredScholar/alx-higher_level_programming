#!/bin/bash
# Displays the length of a url response
curl -I -s "$1" | grep -i "content-length" | cut -d' ' -f2
