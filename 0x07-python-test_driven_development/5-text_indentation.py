#!/usr/bin/python3
""" function to a test """


def text_indentation(text):
    """ returns a text with 2 new lines after each of these char .? :"""
    space = 0
    if type(text) != str:
        raise TypeError("text must be a string")
    for index, value in enumerate(text):
        if value == '.' or value == '?' or value == ':':
            print('{}{}'.format(value, '\n'))
            if text[index + 1] == ' ':
                space = 1
        else:
            if space == 1:
                space = 0
                continue
            print(value, end='')
