#!/usr/bin/python3 


def safe_print_list(my_list=[], x=0):
    str_len = 0
    for i in range(x):
        try:
            print(my_list[i], end='')
            str_len += 1
        except Exception as error:
            break
    print('')
    return str_len

