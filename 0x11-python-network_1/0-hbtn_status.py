#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status"""
if __name__ == "__main__":
    from urllib.request import urlopen
    url = 'https://alx-intranet.hbtn.io/status'
    with urlopen(url) as response:
        script = response.read()
        print("- type: {}".format(type(script)))
        print("- content: {}".format(script))
        print("- utf8 content: {}".format(script.decode('utf-8')))
