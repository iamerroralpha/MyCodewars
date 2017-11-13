# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 13:14:40 2017

@author: Gubynator
"""

def friend(x):
    friends = []
    for item in x:
        if (IsFriend(item)):
            friends.append(item)
    return friends