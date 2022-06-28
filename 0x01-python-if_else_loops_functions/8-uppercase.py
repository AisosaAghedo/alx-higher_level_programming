#!/usr/bin/python3
def uppercase(str):
    upper = 0
    for i in str:
        if ord(i) >= 97 and ord(i) <= 123:
            upper = ord(i) - 32
        elif ord(i) < 97 or ord(i) > 123:
            upper = ord(i)
        print("{}".format(chr(upper)))
