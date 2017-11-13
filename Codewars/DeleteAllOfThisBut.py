# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 19:18:36 2017

@author: Gubynator
"""

def DeleteAllOFThisBut(TheOnesToDelete ,ConserveThisMany, Array):
    OverridenElements = 0
    Index = 0
    for elements in Array:
        if (TheOnesToDelete == elements):
            OverridenElements = OverridenElements + 1 
            if (OverridenElements > ConserveThisMany):
                Array.pop(Index)
                return DeleteAllOFThisBut(TheOnesToDelete ,ConserveThisMany, Array)
        Index = Index + 1 
    return Array