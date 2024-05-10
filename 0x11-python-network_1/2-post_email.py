#!/usr/bin/python3
""" A script that takes a URL and an email, sends a POST requests to
    the passed URL with the email as a parameter and displays the response
    decoded in UTF-8 """
from sys import argv
from urllib.request import urlopen, Request
from urllib.parse import urlencode

if __name__ == "__main__":
    email = argv[2]
    data = {}
    data['email'] = email
    data_encoded = urlencode(data)
    data = data_encoded.encode('ascii')
    url = Request(argv[1], data=data)

    with urlopen(url) as res:
        print(res.read().decode('UTF-8'))
