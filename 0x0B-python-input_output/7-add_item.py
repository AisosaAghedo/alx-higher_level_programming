#!/usr/bin/python3
"""
 script that adds all arguments to a Python list,
 and then save them to a file
"""


if __name__ == "__main__":
    save = __import__("5-save_to_json_file").save_to_json_file
    load = __import__("6-load_from_json_file").load_from_json_file
    from sys import argv

    try:
        obj = load("add_item.json")

    except FileNotFoundError:
        obj = []
        save(obj, "add_item.json")
    i = 1

    while i < len(argv):
        obj.append(argv[i])
        i += 1
    save(obj, "add_item.json")
