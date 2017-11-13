# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 15:51:01 2017

@author: Gubynator
"""

def reverseseq(n):
    ReverseSequence = []
    for number in range(n, 0 , -1):
        ReverseSequence.append(number)
    return ReverseSequence

def reverseseq(n):
    return list(range(n, 0, -1))