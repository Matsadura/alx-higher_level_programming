#!/bin/bash
# Sends a request to a URL and displays the body of the response
curl -s -I 0.0.0.0:5000 | grep 'Content-Length' | cut -d ' ' -f 2
