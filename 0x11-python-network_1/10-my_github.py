#!/usr/bin/python3
""" A script that takes your GitHub credentials (username and password)
    and uses the GitHub API to display your id """
import requests
from sys import argv

if __name__ == "__main__":
    auth = (argv[1], argv[2])
    response = requests.get('https://api.github.com/user', auth=auth)
    id = response.json().get('id')
    print(id)
