#!/usr/bin/python3
"""
returns number of lines in file
"""


def write_file(filename="", text=""):
    """ returns the number of chars written to `filename` from `text` """
    with open(filename, 'w', encoding='utf=8') as f:
        return f.write(text)
