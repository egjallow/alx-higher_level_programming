#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    differnt = set()
    for elem in set_1:
        if elem in set_2:
            continue
        else:
            differnt.add(elem)
            differnt.add(elem)
    for elem in set_2:
        if elem in set_1:
            continue
        else:
            differnt.add(elem)
            differnt.add(elem)
            
    return differnt
