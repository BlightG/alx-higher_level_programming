#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) != 0:
        wavg = wsum = 0
        for x in my_list:
           wavg = (x[0] * x[1]) + wavg
        for x in my_list:
            wsum = wsum + x[1]
        wavg = wavg / wsum 
        return wavg
    else:
        return 0
