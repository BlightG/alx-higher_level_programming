#!/usr/bin/python3
"""module to fin peak from list of int """


def find_peak(list_of_integers):
    """a funtion to find max number"""
    if len(list_of_integers) == 0:
        return None

    peak = list_of_integers[0]
    for i in list_of_integers:
        if peak < i:
            peak = i

    return peak
