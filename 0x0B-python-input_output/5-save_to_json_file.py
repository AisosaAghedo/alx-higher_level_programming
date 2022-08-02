#!/usr/bin/python3
"""
 function that writes an Object to a text file
 using a JSON representation
 """


from json import dump


def save_to_json_file(my_obj, filename):
    """ returns json """
    with open(filename, 'w', encoding="utf-8") as f:
        return dump(my_obj, f)
