#!/bin/bash
# Sends a POST request and displays the body of the respose
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
