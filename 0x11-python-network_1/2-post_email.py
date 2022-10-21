#!/usr/bin/python3
"""  Python script that takes in a URL and an email, sends
a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)"""
if __name__ == '__main__':
    import urllib.request as request
    import urllib.parse as parse
    from sys import argv
    url = argv[1]
    value = {'email': argv[2]}
    data = parse.urlencode(value).encode('ascii')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        script = response.read()
        print(script.decode('utf-8'))
