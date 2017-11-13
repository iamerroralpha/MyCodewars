# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 16:02:22 2017

@author: Gubynator
"""

def likes(names):
    NumberOfPersons = HowManyPersons(names)
    if (NumberOfPersons == 0):
        return ('no one likes this')
    else:
        if (NumberOfPersons == 1):
            return (names[0]+' likes this')
        else:
            if (NumberOfPersons == 2):
                return (names[0] + ' and ' + names[1] + ' like this')
            else:
                if (NumberOfPersons == 3):
                    return (names[0] + ', ' + names[1] + ' and ' + names[2] + ' like this')
                else:
                    return (names[0] + ', ' + names[1] + ' and ' + str(NumberOfPersons-2) + ' others like this')
                    


def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }
    [min(4, n)].format(*names[:3], others=n-2)