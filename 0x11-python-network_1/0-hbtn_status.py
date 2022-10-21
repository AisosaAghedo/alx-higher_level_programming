#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status"""
if __name__ == "__main__":
    from urllib.request import urlopen
    url = 'https://alx-intranet.hbtn.io/status'
    with urlopen(url) as response:
        script = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(script)))
        print("\t- content: {}".format(script))
        print("\t- utf8 content: {}".format(script.decode('utf-8')))
