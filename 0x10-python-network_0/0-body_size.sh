#!/bin/bash
# Sends a request to a URL and displays the body of the response
curl -s -I "$2" | grep 'Content-Length' | cut -d ' ' -f 2
