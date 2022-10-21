#!/usr/bin/python3
""" Please list 10 commits (from the most recent to oldest) of
the repository “rails” by the user “rails”You must use the GitHub API,
here is the documentation https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)"""
if __name__ == '__main__':
    import requests
    from sys import argv
    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])
    r = requests.get(url)
    x = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                x[i]["sha"],
                x[i]["commit"]["author"]["name"]))
    except IndexError:
        pass
