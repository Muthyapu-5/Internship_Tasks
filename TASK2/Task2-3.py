#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 11:48:40 2021

@author: shivakesh
"""

def average(array):
    # your code goes here
    sum_array = sum(set(array))
    len_array = len(set(array))
    output = sum_array/len_array
    return output;
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)