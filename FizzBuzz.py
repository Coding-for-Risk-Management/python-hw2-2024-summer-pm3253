#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 05:22:40 2024

@author: mupeiyao
"""


import numpy as np

def FizzBuzz(start, finish):
    numvec = np.arange(start, finish + 1)
    objvec = np.array(numvec, dtype=object)
    
    objvec[numvec % 3 == 0] = 'fizz'
    objvec[numvec % 5 == 0] = 'buzz'
    objvec[(numvec % 3 == 0) & (numvec % 5 == 0)] = 'fizzbuzz'
    
    return objvec

# Example usage
start = 31
finish = 45
result = FizzBuzz(start, finish)
print(result)