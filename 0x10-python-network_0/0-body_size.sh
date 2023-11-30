#!/bin/bash
# Displays the length of a url response
 curl -I -s "$1" | grep "content-length" | cut -d' ' -f2
