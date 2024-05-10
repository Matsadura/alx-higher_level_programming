#!/usr/bin/python3
""" Lists 10 commits from most recent to oldest """
import requests
from sys import argv

if __name__ == "__main__":
    url = f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits"
    response = requests.get(url)
    response = response.json()
    commits = []
    for i in range(10):
        try:
            sha = response[i]['sha']
            author = response[i]['commit']['author']['name']
            print("{}: {}".format(sha, author))
        except IndexError:
            pass
