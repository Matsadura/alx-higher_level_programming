#!/usr/bin/python3
""" A script that fetches https://alx-intranet.hbtn.io/status """
import requests

if __name__ == "__main__":
    response = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(response.text.__class__))
    print("\t- content: {}".format(response.text))
