#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_list = []
    result = 0
    for i in my_list:
        if i in new_list:
            continue
        new_list.append(i)
    for j in new_list:
        result = result + j
    return result
