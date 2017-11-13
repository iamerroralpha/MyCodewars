# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 13:42:35 2017

@author: Gubynator
"""

def divisors(n):
    return [i for i in range(2, n) if not n % i] or '%d is prime' % n