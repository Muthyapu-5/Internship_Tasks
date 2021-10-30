#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 15:04:20 2021

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