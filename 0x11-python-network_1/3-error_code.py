#!/usr/bin/python3
"""  Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)"""
if __name__ == '__main__':
    from sys import argv
    from urllib.error import HTTPError
    from urllib.request import urlopen
    url = argv[1]
    try:
        with urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
