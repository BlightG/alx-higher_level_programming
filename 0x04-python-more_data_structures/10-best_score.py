#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        maxx = 0
        for i, x in a_dictionary.items():
            if x > maxx:
                maxx = x
                key = i
        return key
    else:
        return None
