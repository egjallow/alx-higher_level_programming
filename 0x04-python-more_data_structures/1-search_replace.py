#!/usr/bin/python3

def search_replace(my_list, search, replace):
    replace_list = []
    for i in my_list:
        if i == search:
            i = replace
        replace_list.append(i)
    return replace_list
