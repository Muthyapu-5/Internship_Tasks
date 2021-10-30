#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 15:49:42 2021

@author: shivakesh
"""

import numpy
 
def arrays(arr):
    # complete this function
    # use numpy.array
    return(numpy.array(arr[::-1], float))

arr = input().strip().split(' ')
result = arrays(arr)
print(result)