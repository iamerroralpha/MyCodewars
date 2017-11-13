# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 13:31:38 2017

@author: Gubynator
"""

def divisors(integer):
    ItsDivisors = []
    for number in range (2,integer-1):
        if (integer % number == 0):
            ItsDivisors.append(number)
    if (len(ItsDivisors) == 0):
        return( str(integer)+" is prime" )
    else:
        return ItsDivisors
        