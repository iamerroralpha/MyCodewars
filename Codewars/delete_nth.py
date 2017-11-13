# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 19:11:23 2017

@author: Gubynator
"""

def delete_nth(order,max_e):
    for element in order:
        if (HowManyIn(element, order) > max_e):
            return delete_nth(DeleteAllOFThisBut(element, max_e, order), max_e)
    return order
            

def delete_nth(order,max_e):
    ans = []
    for o in order:
        if ans.count(o) < max_e: ans.append(o)
    return ans