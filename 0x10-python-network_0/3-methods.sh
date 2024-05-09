#!/bin/bash
# Displays all the HTTP methods the server will accept
curl -s -I -X OPTIONS "$1" | grep 'Allow' | cut -d ' ' -f 2-
