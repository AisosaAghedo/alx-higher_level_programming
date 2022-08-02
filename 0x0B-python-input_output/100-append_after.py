#!/usr/bin/python3
"""
function that inserts a line of text to a file,
after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """appends "new_string" after a line containing
    "search_string" in "filename" """
    with open(filename, encoding='utf-8') as f:
        new_list = []
        while True:
            line = f.readline()
            if line == "":
                break
            new_list.append(line)
            if search_string in line:
                new_list.append(new_string)
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(line_list)
