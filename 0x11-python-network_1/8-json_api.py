#!/usr/bin/python3
""" script that takes in a URL, sends a request to the URL
    and displays the body of the response."""
import requests
from sys import argv

if __name__ == "__main__":
    data = {}
    if len(argv) > 1:
        data['q'] = argv[1]
    else:
        data['q'] = ""
    response = requests.post('http://0.0.0.0:5000/search_user', data=data)

    if type(eval(response.text)) is not dict:
        print('Not a valid JSON')
    elif len(eval(response.text).keys()) != len(eval(response.text).values()):
        print('Not a valid JSON')
    elif len(eval(response.text)) == 0:
        print('No result')
    else:
        id = eval(response.text).get('id')
        name = eval(response.text).get('name')
        print('[{}] {}'.format(id, name))
