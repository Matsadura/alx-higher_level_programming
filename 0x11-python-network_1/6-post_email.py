#!/usr/bin/python3
""" script that takes in a URL and an email address,
    sends a POST request to the passed URL with the email as a parameter,
    and finally displays the body of the response. """
import requests
from sys import argv

if __name__ == "__main__":
    data = {}
    data['email'] = argv[2]

    response = requests.post(argv[1], data=data)
    print(response.text)