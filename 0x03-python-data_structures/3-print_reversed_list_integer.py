#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if type(my_list) is list:
        my_list.reverse()
    else:
        return
    for i in my_list:
        print('{:d}'.format(i))
