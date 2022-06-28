#!/usr/bin/python3
def fizzbuzz():
    i = 1
    while i <= 100:
        if (i / 3) and (i / 5):
            print("FizzBuzz", end=' ')
        elif i / 3:
            print("Fizz", end=' ')
        elif i / 5:
            print("Buzz", end=' ')
        else:
            print(i, end =' ')

