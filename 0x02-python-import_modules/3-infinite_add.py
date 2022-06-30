#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    length = len(argv) - 1
    i = 1
    sum_total = 0
    if length == 0:
        print(0)
    else:
        while i <= length:
            sum_total = sum_total + int(argv[i])
            i = i + 1
        print(sum_total)
