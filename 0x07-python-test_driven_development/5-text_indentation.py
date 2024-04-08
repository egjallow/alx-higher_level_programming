#!/usr/bin/python3
""" Text indentation module
"""


def text_indentation(text):
    """ indents a text string

    Prints a newline when '.', ':', or '?' is found. Does not print the
    space(s) or tabs after the designated characters are found. The next
    printable text continues on a newline.

    Args:
        text (str): character string given

    Raises:
        TypeError: text must be a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    for index, x in enumerate(text):
        if x in ['.', ':', '?']:
            print("{:s}\n".format(text[:index + 1].lstrip()))
            text_indentation(text[index + 1:])
            return
    print("{:s}".format(text.lstrip()), end="")
