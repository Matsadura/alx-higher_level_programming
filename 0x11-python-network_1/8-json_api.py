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

    try:
        res = response.json()
        if len(res) == 0:
            print('No result')
        else:
            id = res.get('id')
            name = res.get('name')
            print('[{}] {}'.format(id, name))
    except Exception as e:
        print('Not a valid JSON')
