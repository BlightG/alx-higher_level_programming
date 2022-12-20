#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) == str:
        legend =\
            {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        maxx = intt = 0
        for i in reversed(range(len(roman_string))):
            if roman_string[i] in legend:
                if legend[roman_string[i]] > maxx:
                    maxx = legend[roman_string[i]]
                if legend[roman_string[i]] < maxx:
                    intt = intt - legend[roman_string[i]]
                else:
                    intt = legend[roman_string[i]] + intt
        return intt
    else:
        return 0
