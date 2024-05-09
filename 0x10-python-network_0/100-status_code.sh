#!/bin/bash
# Sends a request and displays the status code of the response
curl -s -o /dev/null -w "%{response_code}" "$1"
