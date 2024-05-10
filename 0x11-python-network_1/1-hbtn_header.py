#!/usr/bin/python3
""" A script that sens a request and displays the value
    of the X-Request-Id variable """
from sys import argv
from urllib.request import urlopen, Request

if __name__ == "__main__":
    try:
        url = Request(argv[1])
        with urlopen(url) as res:
            print(res.info().get('X-Request-Id'))
    except Exception as e:
        pass
