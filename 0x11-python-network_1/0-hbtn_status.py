#!/usr/bin/python3
""" A script that fetches intranet.com/status """
from urllib.request import urlopen, Request

if __name__ == "__main__":
    req = Request('https://alx-intranet.hbtn.io/status')
    with urlopen(req) as res:
        body = res.read()

    print("Body response:\n",
          "\t- type: {}\n".format(body.__class__),
          "\t- content: {}\n".format(body),
          "\t- utf8 content: {}".format(body.decode(encoding='utf-8')))
