#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    comp = 0
    comp_a = ""
    for i in a_dictionary.items():
        a, b = i
        if comp < b:
            comp = b
            comp_a = a
    return comp_a
