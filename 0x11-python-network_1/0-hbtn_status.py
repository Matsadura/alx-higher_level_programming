#!/usr/bin/python3
""" A script that fetches intranet.com/status """
from urllib.request import urlopen, Request

if __name__ == "__main__":
    req = Request('https://alx-intranet.hbtn.io/status')
    with urlopen(req) as res:
        body = res.read()

    print(f"Body response:\n",
          f"\t- type: {body.__class__}\n",
          f"\t- content: {body}\n",
          f"\t- utf8 content: {body.decode(encoding='utf-8')}")
