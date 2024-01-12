#!/bin/usr/python3

def print_reversed_list_integer(my_list=[]):
    len_of_list = len(my_list)

    while len_of_list > 0:
        print("{:d}".format(my_list[len_of_list - 1]))
        len_of_list = len_of_list - 1


if __name__ == "__main__":
    print_reversed_list_integer(my_list=[])
