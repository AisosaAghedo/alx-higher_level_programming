#!/usr/bin/python3
"""
 function that creates an Object from a “JSON file”
"""
from json import load


def load_from_json_file(filename):
    """ creates an object """
    with open(filename, encoding="utf-8") as f:
        return load(f)
