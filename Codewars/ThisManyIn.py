# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 19:12:23 2017

@author: Gubynator
"""

def HowManyIn(element, array):
    ThisMany = 0
    for elements in array:
        if element == elements:
            ThisMany = ThisMany + 1
    return ThisMany