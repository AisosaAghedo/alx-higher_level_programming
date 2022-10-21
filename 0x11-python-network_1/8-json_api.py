#!/usr/bin/python3
""" Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter"""
if __name__ == '__main__':
    import requests
    from sys import argv
    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""
    r = requests.post(url, data={'q': q})
    try:
        rdict = r.json()
        if len(rdict) == 0:
            print("No result")
        else:
            print("[{}] {}".format(rdict['id'], rdict['name']))
    except ValueError:
        print("Not a valid JSON")
