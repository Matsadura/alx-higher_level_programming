#!/bin/bash
# Sends a JSON post request
curl -sX POST -d "$(cat "$2")" -H "Content-Type: application/json" "$1"
