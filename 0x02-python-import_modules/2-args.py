#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    length = len(argv) - 1
    i = 1
    if length == 0:

        print("0 arguments.")
    elif length == 1:
        print("1 argument:")
        print("{:d}: {:s}".format(i, argv[i]))
    else:
        print("{:d} arguments:".format(length))
        while i <= length:
            print("{:d}: {:s}".format(i, argv[i]))
            i = i + 1

           


